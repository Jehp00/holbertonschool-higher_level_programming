#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + args[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
