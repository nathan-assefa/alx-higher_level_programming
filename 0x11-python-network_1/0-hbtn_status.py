#!/usr/bin/python3
""" Fetching data from https://alx-intranet.hbtn.io/status """


if __name__ == "__main__":
    import urllib.request
    """ Fetching data from URL """

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        response = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        # decoding the bytes into python string using decode method
        _str = response.decode('utf-8')
        print("\t- utf8 content: {}".format(_str))
