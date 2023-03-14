#!/usr/bin/node

let occurence = 0
module.logMe = function (item) {
  console.log(`${occurence}: ${item}`);
  occurence += 1
};
