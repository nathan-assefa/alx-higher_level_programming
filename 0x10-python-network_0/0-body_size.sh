#!/bin/bash
# This gets the size of the http reponse in byte
curl -Is -L "$1" | grep -w 'Content-Length' | cut -d ' ' -f2
