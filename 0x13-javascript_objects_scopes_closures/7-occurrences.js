#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((el) => { if (el === searchElement) { count++ } });
  return count;
};
