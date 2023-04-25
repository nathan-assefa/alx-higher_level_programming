#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const result = JSON.parse(body);
    const ans = {};
    for (const res of result) {
      if (res.completed && !ans[res.userId]) {
        ans[res.userId] = 1;
      } else if (res.completed) {
        ans[res.userId] += 1;
      }
    }
    console.log(ans);
  }
});
