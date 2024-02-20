#!/usr/bin/node
const request = require('request');
const apiURL = 'https://swapi-api.alx-tools.com/api/films/$process.argv[2]/';
request.get(apiURL, (error, response, body) => {
  if (error) {
    console.error('Error making the request:', error);
  }
  try {
    const movieData = JSON.parse(body);
    console.log(`characters for Movie ID ${process.argv[2]} - "${movieData.title}":`);
    movieData.characters.forEach(characterUrl => {
      request.get(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error fetching character data:', charError);
        } else {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  } catch (parseError) {
    console.error('Error parsing the API response:', parseError);
  }
});
