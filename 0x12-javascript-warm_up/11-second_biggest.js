#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.slice(2);
  console.log(list.reverse()[1]);
}
