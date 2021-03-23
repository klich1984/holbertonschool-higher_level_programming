#!/usr/bin/node
const myVar = process.argv;

const arg2 = parseInt(myVar[2]);
const arg3 = parseInt(myVar[3]);

function add (a, b) {
  return a + b;
}

const result = add(arg2, arg3);
console.log(result);
