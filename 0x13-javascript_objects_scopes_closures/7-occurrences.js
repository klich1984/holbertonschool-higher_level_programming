#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let ocurences = 0;
  list.forEach(element => {
    if (element === searchElement) {
      ocurences += 1;
    }
  });
  return ocurences;
};
