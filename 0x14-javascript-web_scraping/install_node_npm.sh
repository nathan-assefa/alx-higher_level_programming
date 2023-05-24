#!/usr/bin/env bash
# This script download and install node.js 14 and npm along with request module of node.js

# this is used to download and execute a script from the specified URL
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

sudo apt-get install -y nodejs

# Install request module and use it
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
