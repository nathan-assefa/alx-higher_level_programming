#!/usr/bin/python3
"""
    sends a request to the URL and displays the body
    of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    """ Displaying a response and handling erros """
    r = requests.get(argv[1])
    if r.status_code != 200:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
