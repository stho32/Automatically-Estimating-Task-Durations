function ConvertTo-DPWPreparedModel {
    <#
        .SYNOPSIS
        The raw model that is the result of the simple learning needs to be modified a bit
    #>
    Param(
        [Parameter(Mandatory=$true, ValueFromPipeline=$true)]
        $RawModel
    )

    Process {
        return $RawModel | Group-Object Text
    }
}
