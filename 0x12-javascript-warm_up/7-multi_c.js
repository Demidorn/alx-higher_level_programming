#!/usr/bin/node
const arg = process.argv[2];
const numOfOcurrances = parseInt(arg);

if (!isNaN(numOfOcurrances)) {
  for (let i = 0; i < numOfOcurrances; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
