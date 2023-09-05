# Schedule a daily task to run the script
$trigger = New-ScheduledTaskTrigger -Daily -At 12am
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-ExecutionPolicy Bypass -File C:\path\to\scan.ps1"
Register-ScheduledTask -TaskName "Daily Malware Scan" -Trigger $trigger -Action $action

# Script to scan for malware and viruses
Start-MpScan -ScanType FullScan
$threats = Get-MpThreatDetection
if ($threats.Count -eq 0) {
  Write-Host "No malware or viruses detected."
} else {
  Write-Host "Malware or viruses detected:"
  $threats | Format-Table -AutoSize
}