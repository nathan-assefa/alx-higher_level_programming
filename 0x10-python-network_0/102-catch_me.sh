#!/bin/bash
# This causes the server to respond with a message containing "You got me!", in the body of the response.
curl -s -L -X PUT -d "user_id=98" -H "Origin: Holberton" 0.0.0.0:5000/catch_me
