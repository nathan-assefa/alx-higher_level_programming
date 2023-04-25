#!/usr/bin/node
// reads a file

const fs = require('fs').promises;

fs.readFile(process.argv[2], 'utf8')
  .then(data => {
    console.log(data);
  })
  .catch(err => {
    console.error(err);
  });
