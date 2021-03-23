#!/usr/bin/node
const myVar = process.argv;

console.log(myVar);
length = myVar.length;
console.log("Largo = " + length);

const arg2 = parseInt(myVar[2]);
console.log('arg2 =' + arg2)

const newArr = myVar.slice(2, length);
console.log('newArr = ' + newArr);

const arraSort = newArr.sort();
console.log('arraSort = ' + arraSort);

console.log('penultimo dato = ' + arraSort[arraSort.length - 2]);
