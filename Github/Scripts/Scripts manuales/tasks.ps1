# Get the running processes and sort them by memory usage
$processes = Get-Process | Sort-Object -Descending WorkingSet | Select-Object -First 10

# Display the running processes and their resource usage
Write-Host "Running processes and their resource usage:"
$processes | Format-Table -AutoSize Name, Id, CPU, WorkingSet

# Ask the user if they want to terminate a process
$processToKill = Read-Host "Enter the name of the process you want to terminate (or 'q' to quit):"

# If the user enters 'q', exit the script
if ($processToKill -eq "q") {
  exit
}

# Find the process with the specified name
$process = Get-Process -Name $processToKill -ErrorAction SilentlyContinue

# If the process was found, terminate it
if ($process) {
  $process.Kill()
  Write-Host "Process $($process.Name) terminated."
} else {
  Write-Host "Process not found."
}

# Ask the user if they want to see all processes
$showAll = Read-Host "Do you want to see all running processes? (y/n)"

# If the user enters 'y', show all processes
if ($showAll -eq "y") {
  $allProcesses = Get-Process | Sort-Object -Descending WorkingSet
  Write-Host "All running processes and their resource usage:"
  $allProcesses | Format-Table -AutoSize Name, Id, CPU, WorkingSet
}