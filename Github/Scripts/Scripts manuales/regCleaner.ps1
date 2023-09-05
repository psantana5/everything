# Define the registry key to clean
$registryKey = "HKCU:\Software\ExampleKey"

# Get all subkeys of the registry key
$subkeys = Get-ChildItem -Path $registryKey -Recurse

# Loop through each subkey and remove it
foreach ($subkey in $subkeys) {
    Remove-Item -Path $subkey.PSPath -Recurse
}

# Display a message when the cleaning is complete
Write-Host "Registry cleaning complete."