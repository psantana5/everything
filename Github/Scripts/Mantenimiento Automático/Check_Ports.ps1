$network = Read-Host ("What network do you want to scan?")
$range = Read-Host("What range of IP addresses do you want to scan?")

foreach ($r in $range) {
    $ip = "$network.$r"

    # Check if the IP address is reachable
    if (Test-Connection -Count 1 -ComputerName $ip -Quiet) {

        # Check for open ports using Test-NetConnection cmdlet
        $portStatus = Test-NetConnection -ComputerName $ip -Port 1-65535 -InformationLevel Quiet

        foreach ($status in $portStatus) {
            if ($status.TcpTestSucceeded) {
                Write-Host "$ip port $($status.RemotePort) open"
            }
        }

        # Add more vulnerability checks as needed

    } else {
        Write-Host "$ip is not reachable."
    }
}

    if ($openPorts -contains "192.168.0.1:3389") {
        Write-Host "Recommendation: Consider disabling RDP access from outside the network."
    }

    # Add more recommendations as needed