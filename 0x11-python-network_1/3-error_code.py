#!/usr/bin/python3
""" a python script that prints html status error"""


import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    requeststatus = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(requeststatus) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
            print("Error code:{}".format(e.code))
