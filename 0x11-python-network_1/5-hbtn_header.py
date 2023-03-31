#!/usr/bin/python3
"""
    Sends request to URL and displays the value of the
    X-Request-Id variable found in the header of the response.
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    """ This code fetches the data in a variable """

    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
