#!/usr/bin/python3
""" This script sends some data to a web server using urllib module """


if __name__ == "__mani__":
    """ Encoding the data to be sent and make a request """
    import urllib.request
    import urllib.parse
    from sys import argv

    # First write the query string as a dictionary
    data = {'email': argv[2]}

    # Then the data has to be encoded into standard way
    encoded_data = data.parse.urlencode(data)

    # Thenafter, the data should be bytes, and for that we use one more
    # +method called encod('ascii')
    final_data = encoded_data.encode('ascii') # finally we have standard data

    with urllib.request.urlopen(argv[1], final_data) as res:
        print(res.read().decode('utf-8'))
