#!/bin/bash
# This script desplays the body of the response of GET request
curl -sLX GET  "$1" #since the default method is GET we can omit, curl -sL "$1"
