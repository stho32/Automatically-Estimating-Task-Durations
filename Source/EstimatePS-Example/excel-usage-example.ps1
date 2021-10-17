$estimationBase = "Archiv_2021.xlsx"

$historicData = Import-Excel $estimationBase | ForEach-Object {
    $task = $_
    New-Object -TypeName PSObject -Property @{
        Text = $task.Name
        DurationInSeconds = $task."Time spent" * 60 * 60 # hours to seconds
    }
}

$model = $historicData | Get-DPWModelFromData | Sort-Object -Property Text | Group-Object -Property Text

Get-DPWEstimate -Model $model -DurationInSecondsFor "Some new task" -ProbabilityInPercent 95
