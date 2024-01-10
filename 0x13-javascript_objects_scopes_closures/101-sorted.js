#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};

Object.keys(dict).forEach(function (key) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
});

console.log(newDict);
