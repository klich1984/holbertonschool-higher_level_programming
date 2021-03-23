#!/usr/bin/node
const myVar = process.argv;
console.log(myVar);

console.log(typeof myVar[2]);
console.log(typeof myVar[3]);
console.log(typeof myVar[4]);

let arg2 = Number (myVar[2]);
let arg3 = Number (myVar[3]);
let arg4 = Number (myVar[4]);

console.log(typeof arg2);
console.log(typeof arg3);
console.log(typeof arg4);

console.log(arg2);
var intValue = parseInt(arg2);
console.log(intValue);

if ((process.argv.length === 2) || isNaN (arg2)){
	console.log('Not a number');
} else {
	
}
