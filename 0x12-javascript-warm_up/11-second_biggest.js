#!/usr/bin/node
const args = process.argv.slice(2);
const nums = args.map(arg => parseInt(arg));
const sortNums = nums.sort((a, b) => b - a);
const secondBiggest = sortNums[1] || 0;

console.log(`${secondBiggest}`);