# Get the current date and time
$date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

# Create a new restore point with the current date and time as the description
Checkpoint-Computer -Description "Restore point created on $date"

# Get all restore points and sort them by creation time in descending order
$restorePoints = Get-ComputerRestorePoint | Sort-Object -Property CreationTime -Descending

# Delete all but the most recent restore point
if ($restorePoints.Count -gt 1) {
  $restorePoints[1..($restorePoints.Count - 1)] | Remove-ComputerRestorePoint
}