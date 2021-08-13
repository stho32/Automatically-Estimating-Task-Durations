function Get-DPWEstimate {
    <#
        .SYNOPSIS
        estimate a given sequence of words using the given model data
        .EXAMPLE
        Get-DPWEstimate -Model $model -DurationInSecondsFor "Another one bites the dust" -ProbabilityInPercent 90
    #>
    Param(
        [Parameter(Mandatory=$true)]
        $Model,
        [Parameter(Mandatory=$true)]
        $DurationInSecondsFor,
        [Parameter(Mandatory=$true)]
        $ProbabilityInPercent
    )

    Process {
        $split = Get-DPWSplit -Text $DurationInSecondsFor

        $wordsEstimated = $split | ForEach-Object {
            $word = $_
            $dataForWord = $Model | Where-Object Name -eq $word

            if ([bool]$dataForWord) {
                $randomSamples = 1..100 | ForEach-Object {
                    ($dataForWord.Group | Get-Random).DurationInSeconds
                } | Sort-Object

                New-Object -TypeName PSObject -Property @{
                    Text = $word
                    DurationInSeconds = $randomSamples[$ProbabilityInPercent]
                }
            }
        }

        ($wordsEstimated.DurationInSeconds | Measure-Object -Sum).Sum
    }
}
