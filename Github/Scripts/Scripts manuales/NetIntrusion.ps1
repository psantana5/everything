$threshold = 10 # Set the threshold for number of connections
$connections = Get-NetTCPConnection # Get the current TCP connections

# Group the connections by remote IP address and count the number of connections
$grouped = $connections | Group-Object -Property RemoteAddress | Select-Object Name, Count

# Filter the groups to only include those with more than the threshold number of connections
$suspicious = $grouped | Where-Object { $_.Count -gt $threshold }

# If there are any suspicious groups, print a message with the details
if ($suspicious) {
  Write-Host "Possible network intrusion detected:"
  $suspicious | Format-Table -AutoSize
}