#!/usr/bin/node
const request = require('request-promise');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url)
  .then((body) => {
    const characters = JSON.parse(body).characters;
    const promises = characters.map((charUrl) => {
      return request(charUrl).then((charBody) => {
        const name = JSON.parse(charBody).name;
        return name;
      });
    });
    return Promise.all(promises);
  })
  .then((names) => {
    names.forEach((name) => {
      console.log(name);
    });
  })
  .catch((error) => {
    console.error(error);
  });
