#!/usr/bin/node
const args = process.argv.slice(2);
let count = 0;
const messege = 'No argument';

for (count in args) {
  count += 1;
}

args.forEach(function (args) {
  console.log(args);
});
if (count === 0) {
  console.log(messege);
}
