#!/bin/bash
# displays body of response if 200 status
if [ $(curl -sI -L "$1" | grep HTTP | cut -b 10-13 | tail -n 1) -eq 200 ]; then curl -s -L "$1";fi
