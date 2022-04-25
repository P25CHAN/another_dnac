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

def get_network_vLANs(apikey, host):
    url = f"https://{host}/dna/intent/api/v1/topology/vlan/vlan-names"
    payload = None
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Auth-Token": f"{apikey}"
    }

    response_dna = requests.request('GET', url, headers=headers, data = payload, verify=False)
    print(response_dna.text.encode('utf8'))

def main():
    host, username, password = get_username_and_password()
    token = get_token(host, username, password)
    get_network_vLANs(token, host)

if __name__== "__main__":
    main()
