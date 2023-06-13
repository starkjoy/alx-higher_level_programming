#!/usr/bin/node
module.export = class Rectangle {
	constructor (w, h) {
		if (w <= 0 || h <= 0) {
			return {};
		}

		this.width = w;
		this.height = h;
	}

	print() {
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
