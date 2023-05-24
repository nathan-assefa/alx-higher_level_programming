#!/usr/bin/env bash
# This script download and install node.js 14 and npm along with request module of node.js

# this is used to download and execute a script from the specified URL
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

sudo apt-get install -y nodejs

# Install request module and use it
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
# Remember that If you set an environmental variable using the export command
# in a terminal session, it will only be applied to that specific session and
# any child processes spawned from it. When you open a new terminal session,
# the environment variables from the previous session are not inherited.
# So in order to fix that, you can set the environmental variable in the
# '.bashrc file'. This file is sourced automatically when a new interactive
# Bash session starts. By adding the export command to the .bashrc file,
# the variable will be set for every new terminal session.the shell automatically
# sources the .bashrc file to load any defined configurations.
# This ensures that your customizations are applied each time you open a new
# terminal or start a new Bash session.
