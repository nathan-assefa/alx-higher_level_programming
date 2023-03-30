#!/bin/bash
# This script POST request to the passed URL, and displays the body of the response
curl -s -L -d '{"email: test@gmail.com, variable: I will always be here for PLD"}' -X POST "$1" 
