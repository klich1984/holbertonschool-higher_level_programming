#!/usr/bin/node
const myVar = process.argv;

const length = myVar.length;

if (length <= 3) {
  console.log(0);
} else {
  const newArr = myVar.slice(2, length);
  let unicos = Array.from(new Set(newArr));
  unicos = unicos.sort();
  console.log(unicos[unicos.length - 2]);
}
