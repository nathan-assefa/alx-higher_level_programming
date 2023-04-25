#!/usr/bin/node
const request = require('request');

function printCharacters(characters, index) {
  if (index === characters.length) {
    return;
  }
  request(characters[index], function (error, response, body) {
    if (!error && response.statusCode === 200) {
      console.log(JSON.parse(body).name);
    } else {
      console.error('Failed to get character:', characters[index]);
    }
    printCharacters(characters, index + 1);
  });
}

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  } else {
    console.error('Failed to get movie:', process.argv[2]);
  }
});
