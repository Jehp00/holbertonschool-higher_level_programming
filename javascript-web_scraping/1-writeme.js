#!/usr/bin/node
const args = process.argv.slice(2);
const file = args[0];
const text = args[1];

const fs = require('fs');

fs.writeFile(file, text, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  }
});
