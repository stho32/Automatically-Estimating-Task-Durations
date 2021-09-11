function SweArchiv2020() {
    $data = Get-Content "$PSScriptRoot/../../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2020.csv" | ConvertFrom-Csv
    $data | ForEach-Object {
        $row = $_

        if ( [bool]($row."Time Spent") ) {
            New-Object -TypeName PSObject -Property @{
                Text = $row.Name
                Color = $row.Color
                DurationInSeconds = [decimal]::Parse(($row."Time Spent").Replace(".", ",")) * 60 * 60
            }
        }
    }
}

function SweArchiv2021() {
    $data = Get-Content "$PSScriptRoot/../../../Automatically-Estimating-Task-Durations-Private/SWE-Archiv-2021.csv" | ConvertFrom-Csv
    $data | ForEach-Object {
        $row = $_
        if ( [bool]($row."Time Spent") ) {

            New-Object -TypeName PSObject -Property @{
                Text = $row.Name
                Color = $row.Color
                DurationInSeconds = [decimal]::Parse(($row."Time Spent").Replace(".", ",")) * 60 * 60
            }
        }
    }
}
