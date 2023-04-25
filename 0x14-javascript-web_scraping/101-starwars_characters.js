#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;
  const characterNames = [];

  function printCharacterNames() {
    if (characterNames.length === characters.length) {
      characterNames.forEach((name) => console.log(name));
    }
  }

  characters.forEach((url) => {
    request(url, function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }
      const character = JSON.parse(body);
      characterNames[characters.indexOf(url)] = character.name;
      printCharacterNames();
    });
  });
});
