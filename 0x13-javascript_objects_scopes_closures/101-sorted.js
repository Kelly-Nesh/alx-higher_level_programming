#!/usr/bin/node

const { dict } = require('./101-data.js');
const set = new Set(Object.values(dict));
const newdict = {};
for (const i of set) {
  const list = [];
  for (const k of Object.keys(dict)) {
    if (dict[k] === i) {
      list.push(`${k}`);
    }
    newdict[i.toString()] = list;
  }
}
console.log(newdict);
