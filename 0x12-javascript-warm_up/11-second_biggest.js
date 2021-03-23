#!/usr/bin/node
const myVar = process.argv;

const length = myVar.length;

if (length <= 3) {
  console.log(0);
} else {
  let newArr = myVar.slice(2, length);
  newArr = newArr.sort();
  console.log(newArr[newArr.length - 2]);
}
