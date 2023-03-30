#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -s -L -d "$@" -H "Content-Type: application/json" -X POST "$1"
