#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const occurrences = list.reduce((count, element) => {
    if (element === searchElement) {
      return count + 1;
    } else {
      return count;
    }
  }, 0);

  return occurrences;
};
