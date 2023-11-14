#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    this.rect = [];
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        this.rect.push('X');
      }
      if (i !== this.height - 1) { this.rect.push('\n'); }
    }
    console.log(this.rect.join(''));
  }
}

module.exports = Rectangle;
