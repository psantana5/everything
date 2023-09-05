import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes('Hello from the Honeypot!', 'utf8'))
        print(f"GET request received from {self.client_address[0]}")

def start_honeypot(port):
    handler_object = MyHttpRequestHandler
    my_server = socketserver.TCPServer(("localhost", port), handler_object)
    print(f"Honeypot started on port {port}")
    my_server.serve_forever()

if __name__ == "__main__":
    start_honeypot(8000)
