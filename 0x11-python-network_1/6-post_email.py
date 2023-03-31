#!/usr/bin/python3
""" This script sends some data to a web server using requests module """


if __name__ == "__main__":
    """ Since we use requests module, the data would be
    encoded automatically """

    import requests
    from sys import argv

    print(requests.post(argv[1], data={'email': argv[2]}).text)
