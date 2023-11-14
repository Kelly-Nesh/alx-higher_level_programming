#!/usr/bin/node

exports.converter = function (base) {
  function baseint (num) {
    return num.toString(base);
  }
  return baseint;
};
