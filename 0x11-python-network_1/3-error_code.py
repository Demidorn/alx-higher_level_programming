#!/usr/bin/python3
""" a python script that prints html status error"""


from urllib import request, error
import sys


if __name__ == "__main__":
    argv = sys.argv
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.status))
