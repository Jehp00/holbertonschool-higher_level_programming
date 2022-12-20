#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const char = 'X';
    for (let i = 0; i <= this.height - 1; i++) {
      let Rect = '';
      for (let j = 0; j <= this.width - 1; j++) {
        Rect += char;
      }
      console.log(Rect);
    }
  }
};
