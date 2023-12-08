#!/usr/bin/python3
"""Sends a POST request to a given URL
"""
import sys
import urllib.parse as up
import urllib.request as rq


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = up.urlencode(value).encode("ascii")

    request = rq.Request(url, data)
    with rq.urlopen(request) as res:
        print(res.read().decode("utf-8"))
