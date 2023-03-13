#!/usr/bin/node

const X = process.argv[2];
if (isNaN(X)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(X); i++) {
    console.log('X'.repeat(parseInt(X)));
  }
}
