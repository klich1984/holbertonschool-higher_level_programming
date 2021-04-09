#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.
curl -s $1 -I | grep -Fi Allow | cut -d " " -f 2-
