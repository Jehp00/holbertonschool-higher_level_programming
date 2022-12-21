#!/usr/bin/node
const file = process.argv.slice(2);
const fs = require('fs');

if (!file[0]) {
  console.log('');
} else {
  fs.readFile(file[0], 'utf-8', function (err, data) {
    if (!data) {
      console.log(err);
    }
    console.log(data);
  });
}
