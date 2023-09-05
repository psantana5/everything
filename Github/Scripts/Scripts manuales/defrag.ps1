# Get disk health before defrag
$before = Get-Volume -DriveLetter C | Select-Object -Property FileSystemLabel, HealthStatus
# Get list of disks
$disks = Get-Volume | Select-Object -Property DriveLetter, FileSystemLabel

# Prompt user to select disk
$selectedDisk = Read-Host "Select disk to defrag (enter drive letter)"

# Defrag selected disk
Optimize-Volume -DriveLetter $selectedDisk -Defrag -Verbose

# Get disk health after defrag
$after = Get-Volume -DriveLetter C | Select-Object -Property FileSystemLabel, HealthStatus

# Compare disk health before and after defrag
Write-Host "Disk health before defrag: $($before.HealthStatus)"
Write-Host "Disk health after defrag: $($after.HealthStatus)"