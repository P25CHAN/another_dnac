# Module import
import requests
from requests.auth import HTTPBasicAuth

# Disable SSL warnings. Not needed in production environments with valid certificates
import urllib3
urllib3.disable_warnings()

# Authentication
BASE_URL = 'https://198.18.129.100'
AUTH_URL = '/dna/system/api/v1/auth/token'
USERNAME = 'admin'
PASSWORD = 'C!sco12345!@'

response = requests.post(BASE_URL + AUTH_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD), verify=False)
print(response.json()['Token'])
