#!/usr/bin/node

const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    }
    else {
      for (let i = 0; i < this.height; i++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
