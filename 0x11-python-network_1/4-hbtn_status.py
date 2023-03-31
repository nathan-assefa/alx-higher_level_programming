#!/usr/bin/python3
"""
    Write a Python script that fetches
    https://alx-intranet.hbtn.io/status, and here we use
    request module instead of urllib
    Make sure you install the package via pip 'python pip -m install request'
"""


if __name__ == "__main__":
    import requests
    """ Displaying a URL with request module """

    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(str(response))))
    print("\t- content: {}".format(response.text))
