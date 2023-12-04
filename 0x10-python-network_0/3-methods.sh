#!/bin/bash
# checks for allowed methods
curl -sI "$1" | grep "Allow" | cut -b 8-
