#!/usr/bin/node
let ans = 0;
num = parseInt(process.argv[2]);
function factorial(num) {
  if(num === 1) {
    return (1);
  } ans += factorial(num - 1);
}
