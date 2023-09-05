import requests
from tkinter import Tk
from tkinter.filedialog import askopenfilename

url = 'https://www.virustotal.com/vtapi/v2/file/scan'
params = {'apikey': '74abc9944b2db4644d9cf541b032ea74e900a03ae0a0f6b4a298a9dfcd1ddd5c'}

root = Tk()
root.withdraw()
file_path = askopenfilename()

try:
    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files, params=params)
except FileNotFoundError:
    print('The file does not exist in the specified directory.')
    exit()

resource = response.json()['resource']

url = 'https://www.virustotal.com/vtapi/v2/file/report'
params = {'apikey': '74abc9944b2db4644d9cf541b032ea74e900a03ae0a0f6b4a298a9dfcd1ddd5c', 'resource': resource}

response = requests.get(url, params=params)

if response.json()['response_code'] == 0:
    print('The file is not in VirusTotal database.')
else:
    positives = response.json()['positives']
    total = response.json()['total']
    if positives / total > 0.1:
        print('The file is likely a virus.')
    else:
        print('The file is not a virus.')