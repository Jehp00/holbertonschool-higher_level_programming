#!/usr/bin/node
let index = -1;
exports.logMe = function (item) {
  index++;
  console.log(index + ': ' + item);
};
