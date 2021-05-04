#!/usr/bin/node
// console.log(process.argv);
const myArgs = process.argv;
const fs = require('fs');
fs.readFile(myArgs[2], 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
