#!/usr/bin/python3
"""
    Sends request to URL and displays the value of the
    X-Request-Id variable found in the header of the response.
"""


if __name__ == "__main__":
    import urllib.request
    from sys import argv
    """ This code fetches the data in a variable """

    with urllib.request.urlopen(argv[1]) as res:
        # since the 'get' method only work with dictionary,
        # +we first need to change the headers into dict

        print(dict(res.headers).get('X-Request-Id'))
        # we converted to 'dict' since get only works with dict

        # here we can also use getheader method wich
        # +recieves the key and returns the value
        # print(res.getheader('X-Request-I'))
