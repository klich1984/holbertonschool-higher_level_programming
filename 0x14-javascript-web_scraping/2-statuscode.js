#!/usr/bin/node
const myArgs = process.argv;
const request = require('request');

request(myArgs[2], function (error, response) {
  if (error) {
    return console.log(error);
  }
  console.log('code:', response.statusCode); // Print the response status code if a response was received
});
