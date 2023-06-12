#!/usr/bin/node
<<<<<<< HEAD
const argCount = process.argv.length - 2;
if (argCount === 0){
	console.log('No argument');
} else if (argCount === 1) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
=======
console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv[2]);
>>>>>>> 1d0572d42b3f9027454f6be714aa5dee3ae5844d
