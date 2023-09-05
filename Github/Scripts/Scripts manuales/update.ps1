# Get current Windows version
$currentVersion = (Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion").ReleaseId

# Print current Windows version
Write-Host "Current Windows version: $currentVersion"

# Check for updates
$updates = Get-WindowsUpdate -Online

# Install updates
Install-WindowsUpdate -AcceptAll -AutoReboot

# Get new Windows version
$newVersion = (Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion").ReleaseId

# Print new Windows version
Write-Host "New Windows version: $newVersion"

# Get differences between versions
$differences = Invoke-WebRequest "https://docs.microsoft.com/en-us/windows/whats-new/"

# Print differences
Write-Host "Differences between versions:"
$differences.ParsedHtml.getElementsByTagName("h2") | ForEach-Object { $_.innerText }