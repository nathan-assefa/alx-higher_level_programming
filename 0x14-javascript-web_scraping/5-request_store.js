#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) throw new Error(error);
  fs.writeFile(process.argv[3], body, 'utf8', (err) => {
    if (err) throw new Error(err);
  });
});
