#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let noOfOccurences = 0;
  for (const num of list) {
    if (num === searchElement) {
      noOfOccurences += 1;
    }
  }
  return noOfOccurences;
};
