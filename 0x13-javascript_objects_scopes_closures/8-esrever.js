#!/usr/bin/node

exports.esrever = function (list) {
  if (Array.isArray(list)) {
    const listCopy = [];
    list.forEach(element => listCopy.unshift(element));
    return listCopy;
  }
};
