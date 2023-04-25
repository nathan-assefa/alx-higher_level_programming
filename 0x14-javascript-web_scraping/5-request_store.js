#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];

request(url, (error, body) => {
  if (error) throw new Error(error);
  const data = JSON.stringify(body);
  fs.writeFile(process.argv[3], data, 'utf8', (err) => {
    if (err) throw new Error(err);
  });
});
