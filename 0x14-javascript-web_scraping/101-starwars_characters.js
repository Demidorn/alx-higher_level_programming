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

    movieData.characters.reduce((previousPromise, characterUrl) => {
      return previousPromise.then(() => {
        return new Promise((resolve, reject) => {
          request.get(characterUrl, (charError, charResponse, charBody) => {
            if (charError) {
              console.error('Error fetching character data:', charError);
              reject(charError);
            } else {
              try {
                const characterData = JSON.parse(charBody);
                console.log(characterData.name);
                resolve();
              } catch (charParseError) {
                console.error('Error parsing character data:', charParseError.message);
                reject(charParseError);
              }
            }
          });
        });
      });
    }, Promise.resolve());
  } catch (parseError) {
    console.error('Error parsing the API response:', parseError.message);
  }
});
