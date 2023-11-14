#!/usr/bin/node

exports.esrever = function (list) {
  const newlist = [];
  for (const el of list) {
    newlist.unshift(el);
  }
  return newlist;
};
