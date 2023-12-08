#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request as rq


if __name__ == "__main__":
    url = sys.argv[1]

    request = rq.Request(url)
    with rq.urlopen(request) as res:
        print(dict(res.headers).get("X-Request-Id"))
