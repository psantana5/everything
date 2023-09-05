# Define the menu options
$menuOptions = @{
    "1" = "Backup to Google Drive"
}

# Display the menu and get the user's choice
do {
    Write-Host "`nMenu Options:`n"

    foreach ($option in $menuOptions.GetEnumerator() | Sort-Object Name) {
        Write-Host "$($option.Key): $($option.Value)"
    }

    $choice = Read-Host "`nEnter your choice (1, or Q to quit): "
} until ($choice -match '^[1q]$' -and $choice -ne '')

if ($choice -eq '1') {
    # Prompt user for backup time
    do {
        $backupTime = Read-Host "Enter backup time (HH:mm): "
        $validTime = [DateTime]::TryParseExact($backupTime, 'HH:mm', $null, [System.Globalization.DateTimeStyles]::None, [ref]$null)
        if (!$validTime) {
            Write-Host "Invalid time format. Please enter in HH:mm format."
        }
    } until ($validTime)

    # Schedule task to run at specified time
    $trigger = New-ScheduledTaskTrigger -Daily -At $backupTime
    $action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "<your backup command here>"
    Register-ScheduledTask -TaskName "Daily Backup" -Trigger $trigger -Action $action

    Write-Host "Backup scheduled for daily at $($trigger.StartBoundary.ToShortTimeString())"
}