#!/usr/bin/node
const { list } = require('./100-data.js');
const newlist = list.map((el, idx) => { return el * idx; });
console.log(list)
console.log(newlist);
