#!/usr/bin/node

const num = parseInt(process.argv[2]);
function factorial (n) {
  if (n === 1 || isNaN(n)) {
    return (1);
  } return (n * factorial(n - 1));
}
console.log(factorial(num));
