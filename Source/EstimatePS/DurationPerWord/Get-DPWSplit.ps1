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
