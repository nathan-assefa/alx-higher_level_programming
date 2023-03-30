#!/bin/bash
# This script isplays only the status code of the response form the requested URL
curl -s -L -I "$1" | grep -w 'Stutes' | cut -d ' ' -f2-
