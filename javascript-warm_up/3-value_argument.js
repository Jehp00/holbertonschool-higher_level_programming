#!/usr/bin/node
const args = process.argv;
let message;
let len = 0;

while (len in args) {
  len += 1;
}

if (len > 2) {
  console.log(args[2]);
} else {
  message = 'No argument';
  console.log(message);
}
