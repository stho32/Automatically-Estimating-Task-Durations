#!/snap/bin/pwsh

Set-Location $PSScriptRoot
$ErrorActionPreference = "Stop"
Import-Module "../Source/EstimatePS/EstimatePS.psm1"

. ./tools/DataSources.ps1

$swearchiv2020 = SweArchiv2020
$swearchiv2021 = SweArchiv2021

$training_input = $swearchiv2020 

$model = $training_input | Get-DPWModelFromData | Sort-Object -Property Text | Group-Object -Property Text

function ProcessData($data, $probability, $outputfilepath) {
    $position = 0
    $count = ($data | Measure-Object).Count

    $result = $data | ForEach-Object {
        $position += 1
        $d = $_
        $estimateInSeconds = Get-DPWEstimate -Model $model -DurationInSeconds $d.Text -ProbabilityInPercent $probability

        $r = New-Object -TypeName PSObject -Property @{
           Text = $d.Text
           Color = $d.Color
           DurationInSeconds = $d.DurationInSeconds
           EstimateInSeconds = $estimateInSeconds
        }
        
        Write-Host "$outputfilepath $position/$count $($r.Color) $($r.DurationInSeconds) => $($r.EstimateInSeconds)"
        $r
    }

    $result | Export-Csv -Path "output/$outputfilepath" -NoTypeInformation
}

ProcessData $swearchiv2020 25 "A001_swearchiv2020_swearchiv2020_025.csv"
ProcessData $swearchiv2020 50 "A001_swearchiv2020_swearchiv2020_050.csv"
ProcessData $swearchiv2020 75 "A001_swearchiv2020_swearchiv2020_075.csv"
ProcessData $swearchiv2020 80 "A001_swearchiv2020_swearchiv2020_080.csv"
ProcessData $swearchiv2020 90 "A001_swearchiv2020_swearchiv2020_090.csv"
ProcessData $swearchiv2020 100 "A001_swearchiv2020_swearchiv2020_100.csv"

ProcessData $swearchiv2021 25 "A001_swearchiv2020_swearchiv2021_025.csv"
ProcessData $swearchiv2021 50 "A001_swearchiv2020_swearchiv2021_050.csv"
ProcessData $swearchiv2021 75 "A001_swearchiv2020_swearchiv2021_075.csv"
ProcessData $swearchiv2021 80 "A001_swearchiv2020_swearchiv2021_080.csv"
ProcessData $swearchiv2021 90 "A001_swearchiv2020_swearchiv2021_090.csv"
ProcessData $swearchiv2021 100 "A001_swearchiv2020_swearchiv2021_100.csv"


