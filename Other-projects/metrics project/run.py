from flask import Flask, render_template
import psutil
import netifaces

app = Flask(__name__)

@app.route('/metrics')
def get_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    network_stats = psutil.net_io_counters()
    network_bytes_sent = network_stats.bytes_sent / (1024 * 1024)  # Convert to MB/s
    network_bytes_received = network_stats.bytes_recv / (1024 * 1024)  # Convert to MB/s

    metrics = {
        'cpu_percent': cpu_percent,
        'memory_usage': memory_usage,
        'network_bytes_sent': round(network_bytes_sent, 2),
        'network_bytes_received': round(network_bytes_received, 2),
    }
    return metrics


if __name__ == '__main__':
    app.run(debug=True)
