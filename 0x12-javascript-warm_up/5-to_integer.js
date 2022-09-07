#!/usr/bin/node

const argv = process.argv;

const entry = Math.floor(argv[2]);

if (isNaN(entry)) {
 console.log('Not a number');
} else {
 console.log(`My number: ${entry}`);
}
