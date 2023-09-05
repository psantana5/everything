#MUST HAVE SYSMON INSTALLED / PAU SANTANA

# Set the start and end times for the report (4 hours ago to now)
$endTime = Get-Date
$startTime = $endTime.AddHours(-4)

# Get all Sysmon events within the specified time range
$events = Get-WinEvent -FilterHashtable @{
    LogName='Microsoft-Windows-Sysmon/Operational'
    StartTime=$startTime
    EndTime=$endTime
}

# Output a summary of the events
Write-Host "Sysmon events from $($startTime.ToString('yyyy-MM-dd HH:mm:ss')) to $($endTime.ToString('yyyy-MM-dd HH:mm:ss')):`n"

foreach ($event in $events) {
    Write-Host "Event ID: $($event.Id)"
    Write-Host "Provider Name: $($event.ProviderName)"
    Write-Host "Message: $($event.Message)`n"
}