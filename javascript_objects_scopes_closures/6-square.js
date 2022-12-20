#!/usr/bin/node
const firstSquare = require('./5-square');
class Square extends firstSquare {
  charPrint (c) {
    let char = c;
    if (c === undefined) {
      char = 'X';
    }
    for (let i = 0; i <= this.height - 1; i++) {
      let Rect = '';
      for (let j = 0; j <= this.width - 1; j++) {
        Rect += char;
      }
      console.log(Rect);
    }
  }
}

module.exports = Square;
