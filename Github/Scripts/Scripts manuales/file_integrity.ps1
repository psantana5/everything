# Print tips on how to keep computer safe
Write-Host "Tips to keep your computer safe:"
Write-Host "- Keep your operating system and software up-to-date"

# Prompt user to select drive
$selectedDrive = Read-Host "Select drive to check file integrity (enter drive letter)"

# Get file list
$fileList = Get-ChildItem -Path "$selectedDrive\" -Recurse -File

# Get total number of files
$fileNumber = $fileList.Count

# Set up progress bar
$counter = 0
$percent = 0

# Check file integrity
foreach ($file in $fileList) {
    # Update progress bar
    $counter++
    $percent = $counter / $fileNumber * 100
    Write-Progress -Activity "Checking file integrity" -Status "$counter of $fileNumber files checked" -PercentComplete $percent

    # Print tips on how to keep computer safe
    switch ($counter) {
        1 {Start-Sleep -Seconds 7 Write-Host "- Use strong and unique passwords" }
        
        2 {Start-Sleep -Seconds 7 Write-Host "- Install and use anti-virus and anti-malware software" }
     
        3 {Start-Sleep -Seconds 7 Write-Host "- Be cautious when opening email attachments or clicking on links" }
        
        4 {Start-Sleep -Seconds 7 Write-Host "- Use a firewall to block unauthorized access to your computer" }
    }

    Get-FileHash -Path $file.FullName -Algorithm SHA256 | Out-Null
}

# Get disk health
$diskHealth = (Get-Volume -DriveLetter $selectedDrive).HealthStatus

# Print disk health
Write-Host "Disk health: $diskHealth"