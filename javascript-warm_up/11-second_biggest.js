#!/usr/bin/node

const args = process.argv;

function secondBiggest (nums = []) {
  let max = -Infinity; let result = -Infinity;
  for (const v of nums) {
    const nr = Number(v);
    if (nr > max) {
      [result, max] = [max, nr];
    } else if (nr < max && nr > result) {
      result = nr;
    }
  }
  if (result === -Infinity) {
    result = 0;
  }
  return result;
}

console.log(secondBiggest(args));
