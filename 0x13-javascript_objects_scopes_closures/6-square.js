#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c = 'X') {
    this.rect = [];
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        this.rect.push(c);
      }
      if (i !== this.height - 1) { this.rect.push('\n'); }
    }
    console.log(this.rect.join(''));
  }
}
module.exports = Square;
