#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const number of list) {
    if (number === searchElement) {
      count++;
    }
  }
  return count;
};
