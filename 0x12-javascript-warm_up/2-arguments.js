#!/usr/bin/node
let argsCount = process.argv.length - 2;
if (argsCount === 0){
	console.log('No argument');
} else (argsCount === 1) {
	console.log('Argument found');
}
console.log('Arguments found');
