#!/usr/bin/python3
"""Display the value of X-Request-Id."""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
