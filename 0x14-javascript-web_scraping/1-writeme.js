#!/usr/bin/node
const myArgs = process.argv;
const fs = require('fs');
fs.writeFile(myArgs[2], myArgs[3], function (err, data) {
  if (err) {
    return console.log(err);
  }
});
