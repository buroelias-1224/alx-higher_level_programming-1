#!/usr/bin/node

const argv = process.argv;

const convertedVar = Math.floor(argv[2]);

if (isNaN(convertedVar)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < convertedVar; i++) {
    console.log('C is fun');
  }
}
