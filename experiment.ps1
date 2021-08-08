<#
    Experiment Nr. 1 

    Just simply calculate a little bit and have a look on the code that is needed

#>
Set-Location $PSScriptRoot

function Get-DPWSplit {
    <#
        .SYNOPSIS
        this is a simple standardized split for the library
    #>
    Param(
        [Parameter(Mandatory=$true)]
        [string]$Text
    )

    Process {
       if ([bool]$Text) {
           $Text.Split(" :".ToCharArray()) | Where-Object { $_.Trim() -ne "" }
       }
    }
}

function Get-DPWStatistic {
    <#
        .SYNOPSIS
        create simple one word based data that can be used for guessing
    #>
    Param (
        [Parameter(Mandatory=$true, ValueFromPipelineByPropertyName=$true)]
        [string]$Text,
        [Parameter(Mandatory=$true, ValueFromPipelineByPropertyName=$true)]
        [int]$DurationInSeconds
    )

    Process {
        if ([bool]$Text) {
            $split = Get-DPWSplit -Text $Text
            $durationPerWord = $DurationInSeconds / $split.Length

            $split | ForEach-Object {
                $word = $_
                New-Object -TypeName PSObject -Property @{
                    Text = $word
                    DurationInSeconds = $durationPerWord
                }
            }
        }
    }
}

$historicData = Get-Content "SampleInputData.json" | ConvertFrom-Json


$modelData = $historicData | Get-DPWStatistic | Group-Object Text

$modelData

$chance = 90 # n % chance, based on historic data

$guessThis = Read-Host -Prompt "What task do you want performed"
while ([bool]$guessThis) {
    
    $split = Get-DPWSplit -Text $guessThis
    
    $inWords = $split | ForEach-Object {
        $word = $_
        $dataForWord = $modelData | Where Name -eq $word
        
        $randomSamples = 1..100 | ForEach-Object {
            ($dataForWord.Group | Get-Random).DurationInSeconds
        } | Sort-Object

        New-Object -TypeName PSObject -Property @{
            Text = $word
            DurationInSeconds = $randomSamples[$chance] 
        }
    }

    $sum = ($inWords.DurationInSeconds | Measure-Object -Sum).Sum
    $minutes = $sum / 60
    $hours = $minutes / 60

    Write-Host "With $chance % chance I guess that this task will take: $minutes Minutes"

    $guessThis = Read-Host -Prompt "What task do you want performed"
}
 



