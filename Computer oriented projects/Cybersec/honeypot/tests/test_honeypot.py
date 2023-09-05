import unittest
import threading
import urllib.request
import sys
sys.path.append('/honeypot.py')



class TestHoneypot(unittest.TestCase):
    def setUp(self):
        self.port = 8000
        self.server_thread = threading.Thread(target=start_honeypot, args=(self.port,))
        self.server_thread.start()

    def tearDown(self):
        # You would normally stop the server here, but the built-in HTTP server doesn't have a clean way to stop
        pass

    def test_honeypot_response(self):
        response = urllib.request.urlopen(f"http://localhost:{self.port}")
        self.assertEqual(response.status, 200)
        self.assertEqual(response.read(), b'Hello from the Honeypot!')

if __name__ == "__main__":
    unittest.main()
