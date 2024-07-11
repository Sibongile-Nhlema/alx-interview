#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Function to make a request and return a promise
function fetchCharacter (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

// Make an HTTP GET request to the Star Wars API for the specified movie
request(url, async function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  // Get the film data
  const film = JSON.parse(body);

  // Get the list of characters
  const characters = film.characters;

  // Fetch all character names while maintaining order
  try {
    const characterNames = await Promise.all(characters.map(fetchCharacter));
    // Print each character name in the order they come through
    characterNames.forEach(name => console.log(name));
  } catch (err) {
    console.error(err);
  }
});
