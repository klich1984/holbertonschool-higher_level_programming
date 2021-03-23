#!/usr/bin/node
const myVar = process.argv;

const arg2 = parseInt(myVar[2]);

if ((process.argv.length === 2) || isNaN(arg2)) {
  console.log('Missing size');
} else {
  for (let index = 0; index < arg2; index++) {
    console.log('X'.repeat(arg2));
  }
}
