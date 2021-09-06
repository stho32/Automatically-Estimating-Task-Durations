$estimationBase = "$PSScriptRoot\SWE_Archiv_2020.xlsx"

$historicData = Import-Excel $estimationBase | ForEach-Object {
    $task = $_
    New-Object -TypeName PSObject -Property @{
        Text = $task.Name
        DurationInSeconds = $task."Time spent" * 60 * 60 # hours to seconds
    }
}

$model = $historicData | Get-DPWModelFromData | Sort-Object -Property Text | Group-Object -Property Text

$totalError = 0
$count = 0
$totalCount = $historicData | Measure-Object

$result = $historicData | ForEach-Object {
    Write-Host "  - $count / $($totalCount.Count) ..."
    $d = $_
    $estimate = Get-DPWEstimate -Model $model -DurationInSecondsFor $d.Text -ProbabilityInPercent 95
    $squaredError = ($d.DurationInSeconds - $estimate) * ($d.DurationInSeconds - $estimate) 
    $totalError += $squaredError
    $count += 1

    New-Object -TypeName PSObject -Property @{
        Text = $d.Text
        DurationInSeconds = $d.DurationInSeconds
        EstimateInSeconds = $estimate
        SquaredError      = $squaredError
    }
}

$meanSquaredError = [Math]::Round(($totalError / $count), 2)
Write-Host "Mean Squared Error of your model: $meanSquaredError"

$result | Export-Excel -Path "$PSScriptRoot\qa.xlsx"
