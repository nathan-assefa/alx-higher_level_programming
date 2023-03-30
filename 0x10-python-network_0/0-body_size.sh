#!/bin/bash
# This gets the size of the http reponse in byte
curl -Ls "$1" | wc -c
