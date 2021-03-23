#!/usr/bin/node

const BeforeSquare = require('./5-square');

module.exports = class Square extends BeforeSquare {
  charPrint (c) {
    if (c) {
      for (let idx = 0; idx < this.height; idx++) {
        console.log('C'.repeat(this.width));
      }
    } else if (c === undefined) {
      this.print();
    }
  }
};
