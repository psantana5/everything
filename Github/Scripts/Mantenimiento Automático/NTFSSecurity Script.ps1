# Import the NTFSSecurity module
Import-Module -Name NTFSSecurity

# Set the path to the folder or file you want to check permissions for
$folderPath = "C:\Users\Public"

# Get the access rules for the folder or file
$accessRules = Get-NTFSAccess -Path $folderPath

# Output a summary of the access rules
Write-Host "Access rules for $($folderPath):`n"

foreach ($rule in $accessRules) {
    Write-Host "IdentityReference: $($rule.IdentityReference)"
    Write-Host "AccessControlType: $($rule.AccessControlType)"
    Write-Host "FileSystemRights: $($rule.FileSystemRights)`n"
}