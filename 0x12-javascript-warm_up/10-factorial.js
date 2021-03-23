#!/usr/bin/node
const myVar = process.argv;

const arg2 = parseInt(myVar[2]);

function factorial (x) {
  if ( x === 0 ) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

result = factorial(arg2);
console.log(result);
