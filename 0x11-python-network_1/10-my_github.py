#!/usr/bin/python3
""" Uses GitHub API to display a GitHub ID """

import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
