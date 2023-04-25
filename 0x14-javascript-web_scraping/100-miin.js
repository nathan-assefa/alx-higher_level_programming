#!/usr/bin/node

const request = require('request')
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`

request(url, (error, response, body) => {
	if (error) throw new Error(error)

	const resp = JSON.parse(body).characters
	resp.forEach((charName) => {
		request(charName, (error, response, body) => {
			if (error) {
				console.error(error)
				return
			}

			const names = JSON.parse(body).name
			names.forEach((n) => {
				console.log(n)
			})
		})
	})
});
