#!/usr/bin/node
const file = process.argv;
const fs = require('fs');
fs.readFile(file[2], 'utf-8', function (err, data) {
  if (!data) {
    console.log(err);
  }
  console.log(data);
});
