#!/usr/bin/python3
""" sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter. """


if __name__ == "__main__":
    """ Posting a letter to a URL """
    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'

    r = requests.post(url, data={'q': argv[1] if len(argv) > 1 else ""})
    try:
        json = r.json()

        if json:
            print("[{}]: {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
