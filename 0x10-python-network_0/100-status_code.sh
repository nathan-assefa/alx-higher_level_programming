#!/bin/bash
# This script isplays only the status code of the response form the requested URL
curl --silent --head "$1" | awk '/^HTTP/{print $2}'
