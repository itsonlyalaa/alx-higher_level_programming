#!/usr/bin/node

const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (!err) {
    let characters = JSON.parse(body).characters;
    printStarWarsCharacters(characters, 0);
  }
});

function printStarWarsCharacters (characters, index) {
  request(characters[index], function (err, response, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printStarWarsCharacters(characters, index + 1);
      }
    }
  });
}

