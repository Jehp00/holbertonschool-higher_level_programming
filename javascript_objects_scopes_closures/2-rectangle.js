#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (parseInt(w) <= 0 || w === undefined) {
      w = {};
      h = {};
    }
    if (parseInt(h) <= 0 || h === undefined) {
      h = {};
      w = {};
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
