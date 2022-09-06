#!/usr/bin/node

const myVar = process.argv[2];

if (myVar !== null && myVar !== undefined) {
	console.log(myVar);
} else {
	console.log('No argument');
}
