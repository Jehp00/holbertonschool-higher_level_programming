#!/usr/bin/node
const arg = process.argv;
const char = 'X';
const count = Object.keys(arg).length;
let square;

if (isNaN(parseInt(arg[2])) || count === 2) {
  console.log('Missing size');
} else {
  for (let i = 0; i <= parseInt(arg[2]) - 1; i++) {
    square = '';
    for (let j = 0; j <= parseInt(arg[2]) - 1; j++) {
      square += char;
    }
    console.log(square);
  }
}
