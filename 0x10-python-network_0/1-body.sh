#!/bin/bash
# displays body of response if 200 status
status="$(curl -sI -L "$1" | grep HTTP | cut -b 10-13)"; status="$(echo $status | cut -b 5-)"; if [ $status -eq 200 ]; then curl -s -L "$1";fi
