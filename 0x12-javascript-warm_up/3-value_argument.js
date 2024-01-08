#!/usr/bin/node
const firstArgument = process.argv[2];
if (firstArgument === 0){
    console.log("No argument");
} else{
    console.log(`${firstArgument}`);
}