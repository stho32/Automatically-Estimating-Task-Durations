$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Push-Location $PSScriptRoot

Get-ChildItem -Filter "*.ps1" -Recurse | 
	ForEach-Object {
		. ($_.Fullname)
}

Pop-Location
