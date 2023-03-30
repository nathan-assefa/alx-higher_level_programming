#!/bin/bash
# This gets the size of the http reponse in byte
curl -s "$1" | wc -c
