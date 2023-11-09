#!/usr/bin/node
// Script that prints all characters of a Star Wars movie
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line in the SAME ORDER of the list “characters” in the /films/ response
// You must use the Star wars API
// You must use the module request

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function getCharacters (characters) {
  request(characters, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
    }
  });
}

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      getCharacters(character);
    }
  }
});
