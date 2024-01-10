#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || w <= 0 || !Number.isInteger(w) || !Number.isInteger(w)) {
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
