#!/bin/bash
# curl status code only
curl -s -o /dev/null -w "%{http_code}" "$1"
