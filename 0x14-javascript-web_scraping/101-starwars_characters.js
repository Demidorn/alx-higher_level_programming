#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiURL = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(apiURL, (error, response, body) => {
  if (error) {
    console.error('Error making the request:', error);
    return;
  }

  try {
    const movieData = JSON.parse(body);

    if (body.startsWith('<')) {
      console.error('Error from API:', body);
      return;
    }

    console.log(`Characters for Movie ID ${movieId} - "${movieData.title}":`);

    const characterNames = [];

    const fetchAndPrintCharacter = (characterUrl) => {
      request.get(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error fetching character data:', charError);
        } else {
          try {
            const characterData = JSON.parse(charBody);
            characterNames.push(characterData.name);

            if (characterNames.length === movieData.characters.length) {
              characterNames.forEach(name => console.log(name));
            }
          } catch (charParseError) {
            console.error('Error parsing character data:', charParseError.message);
          }
        }
      });
    };

    movieData.characters.forEach(fetchAndPrintCharacter);
  } catch (parseError) {
    console.error('Error parsing the API response:', parseError.message);
  }
});
