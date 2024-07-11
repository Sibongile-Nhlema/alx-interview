#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make an HTTP GET request to the Star Wars API for movie id given
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  // Get the film data
  const film = JSON.parse(body);

  // Get the list of characters
  const characters = film.characters;

  characters.forEach((characterUrl) => {
    // Make an HTTP GET request to get the details for each character
    request(characterUrl, function (charError, charResponse, charBody) {
      if (charError) {
        console.error(charError);
        return;
      }

      // Parse the JSON response body to get the character data
      const character = JSON.parse(charBody);

      console.log(character.name);
    });
  });
});
