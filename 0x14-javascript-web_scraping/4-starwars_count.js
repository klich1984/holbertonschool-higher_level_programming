#!/usr/bin/node
const myArgs = process.argv;
const request = require('request');

request(myArgs[2], function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const info = JSON.parse(body);
  let count = 0;
  // console.log(info.results[0].characters);
  const req = info.results;
  for (const i of req) {
    // console.log(i)
    if (i.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count++;
    }
  }
  // for (let i = 0; i < info.results.length; i++) {
  //   if (info.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
  //     count++;
  //   }
  // }
  console.log(count);
});
