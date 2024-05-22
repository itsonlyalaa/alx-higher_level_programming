#!/usr/bin/node

const request = require('request');
const starWarsUri = process.argv[2];
let times = 0;

request(starWarsUri, function (err, response, body) {
  body = JSON.parse(body).res;

  for (let i = 0; i < body.length; ++i) {
    const characters = body[i].characters;

    for (let y = 0; y < characters.length; ++y) {
      const character = characters[j];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        times += 1;
      }
    }
  }
  console.log(times);
});
