#!/usr/bin/node
const args = process.argv;

function fact (num) {
  if (!(isNaN(num)) && Number(num) > 0) {
    return Number(num) * fact(Number(num) - 1);
  } else {
    return 1;
  }
}
console.log(fact(args[2]));
