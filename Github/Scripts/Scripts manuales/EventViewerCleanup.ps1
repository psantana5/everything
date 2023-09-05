# Define the event logs to clear
$eventLogs = "Application", "System", "Security"

# Loop through each event log and clear it
foreach ($eventLog in $eventLogs) {
    Clear-EventLog -LogName $eventLog
}

# Display a message when the cleaning is complete
Write-Host "Event Viewer cleaning complete."