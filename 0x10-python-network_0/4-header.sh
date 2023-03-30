#!/bin/bash
# This script sends GET request and displays the body of the response
curl -s -I -L "$1"?X-School-User-Id=98
