#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');

request(args[0], (error, response, body) => {
  let films;
  if (error) {
    console.log(error);
  } else {
    films = JSON.parse(body).results;
  }
  let counter = 0;
  for (let i = 0; i < films.length; i++) {
    for (let j = 0; j < films[i].characters.length; j++) {
      if (films[i].characters[j].includes('18')) {
        counter++;
      }
    }
  }
  console.log(counter);
});
