#!/usr/bin/node

const BeforeSquare = require('./5-square');

module.exports = class Square extends BeforeSquare {
  charPrint (c) {
    if (c !== undefined) {
      for (let idx = 0; idx < this.height; idx++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
};
