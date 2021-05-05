#!/usr/bin/node
const myArgs = process.argv;
const request = require('request');
const fs = require('fs');

request(myArgs[2], function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  fs.writeFile(myArgs[3], body, 'utf8', function (error, data) {
    if (error) {
      return console.log(error);
    }
  });
});
