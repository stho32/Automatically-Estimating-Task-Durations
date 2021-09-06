Set-Location $PSScriptRoot

$estimationBase = "$PSScriptRoot\SWE_Archiv_2020.xlsx"
$estimateBase = "$PSScriptRoot\SWE_Archiv_2020.xlsx"

$historicData = Import-Excel $estimationBase | ForEach-Object {
    $task = $_
    New-Object -TypeName PSObject -Property @{
        Text = $task.Name
        DurationInSeconds = $task."Time spent" * 60 * 60 # hours to seconds
    }
} 

$historicData = $historicData | Sort-Object DurationInSeconds
# now we want only the middle 90%, so we need to cut off 5% of the values at the start and the end
$count = ($historicData | Measure-Object).Count
$fivePercent = [int]($count * 0.05)
$historicData = $historicData[$fivePercent..($count-$fivePercent)]

$dataToEstimate = Import-Excel $estimateBase | ForEach-Object {
    $task = $_
    New-Object -TypeName PSObject -Property @{
        Text = $task.Name
        DurationInSeconds = $task."Time spent" * 60 * 60 # hours to seconds
    }
} 

$averageTaskDuration = ($historicData.DurationInSeconds | Measure-Object -Average).Average

$count = 0
$totalCount = $dataToEstimate | Measure-Object
$estimateIsAbove = 0
$totalError = 0

$result = $dataToEstimate | ForEach-Object {
    Write-Host "  - $count / $($totalCount.Count) ..."
    $d = $_
    $estimate = $averageTaskDuration

    $squaredError = ($d.DurationInSeconds - $estimate) * ($d.DurationInSeconds - $estimate) 

    $totalError += $squaredError
    $count += 1

    if ( $estimate -gt $d.DurationInSeconds ) {
        $estimateIsAbove += 1
    }

    New-Object -TypeName PSObject -Property @{
        Text = $d.Text
        DurationInSeconds = $d.DurationInSeconds
        EstimateInSeconds = $estimate
    }
}

Write-Host "Mean Squared Error of your model: $([Math]::Round(($totalError / $count), 2))"

Write-Host "Percent of estimates that are too high: $($estimateIsAbove / $count * 100) %"

if (Test-Path "$PSScriptRoot\qa.xlsx") {
    Remove-Item "$PSScriptRoot\qa.xlsx"
}
$result | Export-Excel -Path "$PSScriptRoot\qa.xlsx"
