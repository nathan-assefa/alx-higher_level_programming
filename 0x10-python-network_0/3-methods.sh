#!/bin/bash
# This script displays all HTTP methods the server will accept.
curl -sI -L -X OPTIONS "$1"
