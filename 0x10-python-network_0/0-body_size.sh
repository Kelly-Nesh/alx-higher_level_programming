#!/bin/bash
# displays content length 
curl -sI "$1" | grep -E "Content-Length" | cut -b 17-
