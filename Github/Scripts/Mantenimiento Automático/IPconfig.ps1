# Display menu
Write-Host "1. Set static IP address"
Write-Host "2. Set IP address through DHCP"
Write-Host "3. See current IP configuration"

# Get user input
$choice = Read-Host "Enter your choice (1, 2, or 3)"

# Set static IP address
if ($choice -eq "1") {
  $ip = Read-Host "Enter IP address"
  $subnet = Read-Host "Enter subnet mask"
  $gateway = Read-Host "Enter default gateway"
  $dns = Read-Host "Enter DNS server address"

  # Configure network settings
  netsh interface ip set address "Ethernet" static $ip $subnet $gateway 1
  netsh interface ip set dns "Ethernet" static $dns
}

# Set IP address through DHCP
if ($choice -eq "2") {
  # Configure network settings
  netsh interface ip set address "Ethernet" dhcp
  netsh interface ip set dns "Ethernet" dhcp
}

# Revise current IP configuration
if ($choice -eq "3") {
  # Display current IP configuration
  netsh interface ip show config "Ethernet"

  # Get user input
  $ip = Read-Host "Enter IP address"
  $subnet = Read-Host "Enter subnet mask"
  $gateway = Read-Host "Enter default gateway"
  $dns = Read-Host "Enter DNS server address"

  # Configure network settings
  netsh interface ip set address "Ethernet" static $ip $subnet $gateway 1
  netsh interface ip set dns "Ethernet" static $dns
}