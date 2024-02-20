#!/usr/bin/node
const request = require('request');

const apiURL = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

request.get(apiURL, (error, response, body) => {
  if (error) {
    console.error('Error making the request:', error);
  }

  try {
    const movieData = JSON.parse(body);

    // Check if the response starts with '<' (indicating HTML error)
    if (body.startsWith('<')) {
      console.error('Error from API:', body);
      return;
    }

    console.log(`Characters for Movie ID ${process.argv[2]} - "${movieData.title}":`);

    movieData.characters.forEach(characterUrl => {
      request.get(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error fetching character data:', charError);
        } else {
          try {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          } catch (charParseError) {
            console.error('Error parsing character data:', charParseError.message);
          }
        }
      });
    });
  } catch (parseError) {
    console.error('Error parsing the API response:', parseError.message);
  }
});
