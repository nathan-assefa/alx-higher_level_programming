#!/bin/bash
# This script isplays only the status code of the response form the requested URL
curl -s -L "$1" | grep -w 'HTTP/1.1' | cat -d ' ' -f2
