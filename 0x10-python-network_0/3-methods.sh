#!/bin/bash
# This script displays all HTTP methods the server will accept.
curl -i -L -X OPTIONS "$1"
