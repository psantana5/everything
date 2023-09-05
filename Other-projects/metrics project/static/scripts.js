function updateMetrics() {
    fetch('/metrics')
        .then(response => response.json())
        .then(data => {
            document.getElementById('cpu-percent').textContent = data.cpu_percent;
            document.getElementById('memory-usage').textContent = data.memory_usage;
            document.getElementById('network-bytes-sent').textContent = data.network_bytes_sent;
            document.getElementById('network-bytes-received').textContent = data.network_bytes_received;
        })
        .catch(error => console.log(error));
}

// Update metrics initially
updateMetrics();

// Update metrics every 5 seconds
setInterval(updateMetrics, 5000);
