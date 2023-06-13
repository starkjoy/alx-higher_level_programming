#!/usr/bin/node
class Square extends Square {
	charPrint(c) {
		if (c === undefined) {
			c = 'X';
		}

		for (let i = 0; i < this.height; i++)
		{
			console.log("X");
			for (let j = 0; j < this.width; j++)
			{
				console.log("X");
			}
		}
	}
}
