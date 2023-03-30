#!/bin/bash
# This gets the size of the http reponse in byte
curl -ILs "$1" | grep -w 'Content-Length' | cat -d ' ' -f2
