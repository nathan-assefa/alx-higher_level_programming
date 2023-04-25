#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) throw new Error(error);
  let count = 0;
  const films = JSON.parse(body).results;
  for (let i = 0; i < films.length; i++) {
    const characters = films[i].characters;
    for (let j = 0; j < characters.length; j++) {
      const character = characters[j];
      if (character.indexOf('/18/') !== -1) {
        count++;
      }
    }
  }
  console.log(count);
});
