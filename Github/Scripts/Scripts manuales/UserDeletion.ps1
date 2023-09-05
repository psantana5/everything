# Define the number of days since last use
$daysSinceLastUse = 30

# Define the user profiles to exclude
$excludedProfiles = "Administrator", "Default", "Public"

# Define the minimum profile size to exclude
$minProfileSize = 500MB

# Get all user profiles on the system
$userProfiles = Get-WmiObject -Class Win32_UserProfile

# Loop through each user profile and check if it meets the criteria for deletion
foreach ($userProfile in $userProfiles) {
    $lastUse = $userProfile.LastUseTime
    $daysSinceLastUse = (New-TimeSpan -Start $lastUse).Days
    if ($userProfile.LocalPath -notmatch $excludedProfiles -and $daysSinceLastUse -gt $daysSinceLastUse) {
        # Backup the user profile
        $backupPath = "C:\Backup\$($userProfile.LocalPath.Split("\")[-1])_$(Get-Date -Format "yyyyMMdd_HHmmss")"
        Robocopy $userProfile.LocalPath $backupPath /E /ZB /COPYALL /DCOPY:T /R:1 /W:1 /LOG+:C:\BackupLog.txt

        # Check the size of the user profile
        $profileSize = (Get-ChildItem -Path $userProfile.LocalPath -Recurse | Measure-Object -Property Length -Sum).Sum
        if ($profileSize -lt $minProfileSize) {
            # Remove the user profile
            $userProfile.Delete()

            # Log the cleanup activity
            $logMessage = "User profile $($userProfile.LocalPath) deleted on $(Get-Date)"
            Add-Content -Path "C:\CleanupLog.txt" -Value $logMessage
        }
    }
}

# Display a message when the cleaning is complete
Write-Host "User profile cleaning complete."