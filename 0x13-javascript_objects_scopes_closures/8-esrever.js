#!/usr/bin/node

exports.esrever = function (list) {
  const listReverse = [];
  for (let i = list.length - 1; i >= 0; i--) {
    listReverse.push(list[i]);
  }
  return listReverse;
};
