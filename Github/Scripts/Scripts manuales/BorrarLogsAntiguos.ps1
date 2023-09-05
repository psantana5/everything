# Check if the script is running with administrator privileges
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

# If the script is not running with administrator privileges, relaunch the script with administrator privileges
if (-not $isAdmin)
{
    Start-Process powershell.exe "-File `"$PSCommandPath`"" -Verb RunAs
    Exit
}
# Set the path to the log files
$logPath = "C:\Logs"

# Set the number of days to keep log files
$daysToKeep = 30

# Get the current date
$currentDate = Get-Date

# Calculate the date to compare against
$compareDate = $currentDate.AddDays(-$daysToKeep)

# Get a list of log files older than the compare date
$logFiles = Get-ChildItem $logPath -Recurse | Where-Object { $_.LastWriteTime -lt $compareDate }

# Delete the old log files
$logFiles | Remove-Item -Force