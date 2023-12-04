#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays 
# the size body of the response
curl -sI "$1" | grep -E "Content-Length" | cut -b 17-
