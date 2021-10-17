<#
    Experiment Nr. 1 

    Just simply calculate a little bit and have a look on the code that is needed

#>
Set-Location $PSScriptRoot
$ErrorActionPreference = "Stop"

Import-Module "../EstimatePS/EstimatePS.psm1"

$inputDataFile = "SampleInputData.json"
$modelFile = "dpw-model.json"

# create a model from the sample data
if (-not(Test-Path $modelFile)) {
    # read prepared data
    $rawdata = Get-Content $inputDataFile | ConvertFrom-json
    # convert it into the way we need it
    $model = $rawData | Get-DPWModelFromData | Sort-Object -Property Text | Group-Object -Property Text
    # save the model data, so we can be faster the next time
    $model | ConvertTo-Json -Depth 100 | Out-File $modelFile -Force
} else {
    # just load the prepared model
    $model = Get-Content $modelFile | ConvertFrom-Json
}

# guess a new task
Get-DPWEstimate -Model $model -DurationInSecondsFor "add a new bookkeeping api" -ProbabilityInPercent 90



