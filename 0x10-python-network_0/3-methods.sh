#!/bin/bash
# checks for allowed methods
curl -sI 0.0.0.0:5000/route_4 | grep "Allow" | cut -b 8-
