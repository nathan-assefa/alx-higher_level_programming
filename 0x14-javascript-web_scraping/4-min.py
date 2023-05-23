#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    let i = 0;
    for (const film of films) {
      const characters = film.characters;
      if (characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        i++;
      }
    }
    console.log(i);
  }
});
