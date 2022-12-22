#!/usr/bin/node
const args = process.argv.slice(2);
const url = args[0];
const file = args[1];
const request = require('request');
const fs = require('fs');

request(url, function (error, response, body) {
  let result;
  if (error) {
    console.log(error);
  } else {
    result = body;
    fs.writeFile(file, result, 'utf-8', (err, data) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
