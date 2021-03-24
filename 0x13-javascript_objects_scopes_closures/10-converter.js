#!/usr/bin/node

exports.converter = function (base) {
  function convBase (num) {
    return num.toString(base);
  }
  return convBase;
};
