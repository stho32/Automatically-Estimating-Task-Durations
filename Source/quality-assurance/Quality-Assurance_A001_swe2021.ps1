Set-Location $PSScriptRoot

$estimationBase = "$PSScriptRoot\SWE_Archiv_2020.xlsx"

$historicData = Import-Excel $estimationBase | ForEach-Object {
    $task = $_
    New-Object -TypeName PSObject -Property @{
        Text = $task.Name
        DurationInSeconds = $task."Time spent" * 60 * 60 # hours to seconds
    }
} | Where-Object DurationInSeconds -lt 100000


$model = $historicData | Get-DPWModelFromData | Sort-Object -Property Text | Group-Object -Property Text

$count = 0
$totalCount = $historicData | Measure-Object
$estimateIsAbove25 = 0
$estimateIsAbove50 = 0
$estimateIsAbove75 = 0
$totalError25 = 0
$totalError50 = 0
$totalError75 = 0

$result = $historicData | ForEach-Object {
    Write-Host "  - $count / $($totalCount.Count) ..."
    $d = $_
    $estimate25 = Get-DPWEstimate -Model $model -DurationInSecondsFor $d.Text -ProbabilityInPercent 25
    $estimate50 = Get-DPWEstimate -Model $model -DurationInSecondsFor $d.Text -ProbabilityInPercent 50
    $estimate75 = Get-DPWEstimate -Model $model -DurationInSecondsFor $d.Text -ProbabilityInPercent 75

    $squaredError25 = ($d.DurationInSeconds - $estimate25) * ($d.DurationInSeconds - $estimate25) 
    $squaredError50 = ($d.DurationInSeconds - $estimate50) * ($d.DurationInSeconds - $estimate50) 
    $squaredError75 = ($d.DurationInSeconds - $estimate75) * ($d.DurationInSeconds - $estimate75) 

    $totalError25 += $squaredError25
    $totalError50 += $squaredError50
    $totalError75 += $squaredError75
    $count += 1

    if ( $estimate25 -gt $d.DurationInSeconds ) {
        $estimateIsAbove25 += 1
    }
    if ( $estimate50 -gt $d.DurationInSeconds ) {
        $estimateIsAbove50 += 1
    }
    if ( $estimate75 -gt $d.DurationInSeconds ) {
        $estimateIsAbove75 += 1
    }

    New-Object -TypeName PSObject -Property @{
        Text = $d.Text
        DurationInSeconds = $d.DurationInSeconds
        EstimateInSeconds25 = $estimate25
        EstimateInSeconds50 = $estimate50
        EstimateInSeconds75 = $estimate75
    }
}

Write-Host "Mean Squared Error of your model with 25% probability: $([Math]::Round(($totalError25 / $count), 2))"
Write-Host "Mean Squared Error of your model with 50% probability: $([Math]::Round(($totalError50 / $count), 2))"
Write-Host "Mean Squared Error of your model with 75% probability: $([Math]::Round(($totalError75 / $count), 2))"

Write-Host "Percent of estimates that are too high with 25% probability: $($estimateIsAbove25 / $count * 100) %"
Write-Host "Percent of estimates that are too high with 50% probability: $($estimateIsAbove50 / $count * 100) %"
Write-Host "Percent of estimates that are too high with 75% probability: $($estimateIsAbove75 / $count * 100) %"

$result | Export-Excel -Path "$PSScriptRoot\qa.xlsx"
