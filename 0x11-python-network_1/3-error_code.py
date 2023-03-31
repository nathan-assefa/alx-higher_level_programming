#!/usr/bin/python3
"""
    sends a request to the URL and displays the body
    of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    from urllib import request, error
    from sys import argv
    """ Displaying a response and handling erros """
    try:
        with request.urlopen(argv[1]) as res:
            print(res.read().decode('utf-8'))
    except error.URLError as e:
        print("Error code: {}".format(e.code))
