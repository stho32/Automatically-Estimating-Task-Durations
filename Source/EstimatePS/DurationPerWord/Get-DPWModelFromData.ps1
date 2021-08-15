function Get-DPWModelFromData {    
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

