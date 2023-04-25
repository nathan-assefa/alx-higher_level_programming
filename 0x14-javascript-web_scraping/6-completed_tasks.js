#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const res = JSON.parse(body);
    const ans = {};
    for (const r of res) {
      // ans.r['userId'] += res.completed ? 1: 0
      if (r.completed && !ans[r.userId]) {
        ans[r.userId] = 1;
      } else if (r.completed) {
        ans[r.userId] += 1;
      }
    }
    console.log(ans);
  }
});
