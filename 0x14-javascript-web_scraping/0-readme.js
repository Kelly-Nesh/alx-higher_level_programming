#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf8', function (err, data) {
  err ? console.log(err) : process.stdout.write(data);
});
