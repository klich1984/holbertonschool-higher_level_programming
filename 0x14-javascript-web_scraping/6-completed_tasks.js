#!/usr/bin/node
const myArgs = process.argv;
const request = require('request');

request(myArgs[2], function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const info = JSON.parse(body);
  const dict = {};
  for (const i of info){
    if (!(i.userId in dict) && i.completed === true) {
      dict[i.userId] = 0;
    }
    if (i.completed === true){
      dict[i.userId] += 1;
    }
    // if (i.completed == true){
    //   count ++;
  }
  console.log(dict)
});
