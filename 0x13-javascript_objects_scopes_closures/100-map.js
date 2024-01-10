#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map(function (arg, index) {
  return arg * index;
});

console.log(list);
console.log(newList);
