#!/bin/bash
# This gets the size of the http reponse in byte

curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
