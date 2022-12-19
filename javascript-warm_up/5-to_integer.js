#!/usr/bin/node
const args = process.argv;
let len = 0;

while (len in args) {
  len += 1;
}
if (len > 2) {
  if (isNaN(args[2])) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + parseInt(args[2]));
  }
} else {
  console.log('Not a number');
}
