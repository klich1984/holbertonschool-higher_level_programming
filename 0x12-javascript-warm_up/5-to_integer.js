#!/usr/bin/node
const myVar = process.argv;

const arg2 = parseInt(myVar[2]);

if ((process.argv.length === 2) || isNaN(arg2)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg2);
}
