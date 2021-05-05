#!/usr/bin/node
const myArgs = process.argv;
const request = require('request');
url = "https://swapi-api.hbtn.io/api/films/" + myArgs[2]

request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  // console.log('code:', response.statusCode);
  const info = JSON.parse(body)
  console.log(info.title)
});
