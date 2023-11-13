#!/usr/bin/node
const { argv } = require('node:process');
let v = argv[2];
v ? console.log(v) : console.log('No argument');
