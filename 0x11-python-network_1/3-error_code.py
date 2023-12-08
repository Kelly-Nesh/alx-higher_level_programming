#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body
"""
import sys
import urllib.error as err
import urllib.request as rq


if __name__ == "__main__":
    url = sys.argv[1]

    request = rq.Request(url)
    try:
        with rq.urlopen(request) as res:
            print(res.read().decode("ascii"))
    except err.HTTPError as e:
        print("Error code: {}".format(e.code))
