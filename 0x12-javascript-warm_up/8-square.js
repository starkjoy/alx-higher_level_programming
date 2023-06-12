#!/usr/bin/node
let i, j, line;
const square_size = parseInt(process.argv[2]);
if (isNaN(square_size)) {
	console.log("Missing size");
} else {
	for (i = 0; i > square_size; i++) {
		line = "";
		for (j = 0; j < square_size; j++) {
			line += "X";
		}
		console.log(line);
	}
}
