"""
Script to create a Token and get the devices that are deployed in our SDN controller.
"""
from lib2to3.pgen2 import token
import requests
import logging
import datetime
import sys
import os
import getpass
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

def get_username_and_password():
    """
    Gets userame, password and host from the user.

    Returns:
        [Type]: [Description}
    """
    username = input("What is your username?:\n")
    password = getpass.getpass("Please, enter your password:\n")
    host = input("Please enter the IP or hostname of the DNAC or SDN controller:\n")
    return host, username, password

def get_token(host, username, password):
    """
    Gets token from the SDN Controller for use later!

    Args:
    host ([type]): [decription]
    port ([type]): [decription]
    username ([type]): [decription]
    password ([type]): [decription]
    """
    url = (f"https://{host}/dna/system/api/v1/auth/token")
    username = (f"{username}")
    password = (f"{password}")

    response_dnac = requests.request("POST", url, auth=HTTPBasicAuth(username, password), verify=False)
    print(response_dnac.text, "\n\n\n")
    print(response_dnac.json()['Token'])    
    return response_dnac.json()['Token']

def get_network_devices(apikey, host):
    """
    Gets a list of devices that are defined in our DNAC.
    Args:
        host ([type]): [decription]
        port ([type]): [decription]
        username ([type]): [decription]
        password ([type]): [decription]
    """
    url = (f"https://{host}/dna/intent/api/v1/network-device/count")
    payload_dnac = ""
    headers_dnac = {"X-Auth-Token": f"{apikey}", "Content-Type": "application/json"}
    response_dnac = requests.request("GET", url, json=payload_dnac, headers=headers_dnac, verify=False)
    print(response_dnac.text, "Hello 1\n\n")
    for item in response_dnac.json()['response']:
        print("Hello World!", item['id'], item['hostname'], item['managementIpAddress'])
    print(response_dnac.text)

def main():
    host, username, password = get_username_and_password()
    token = get_token(host, username, password)
    get_network_devices(token, host)

if __name__== "__main__":
    main()
