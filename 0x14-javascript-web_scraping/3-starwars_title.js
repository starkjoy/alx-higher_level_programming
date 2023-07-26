#!/usr/bin/node
const request = require('request');
let url = 'http://swapi.co/api/films/' + process.argv[2]
request(url, (error, response, body) => {
	console.log(error || JSON.parse(body).title);
});
