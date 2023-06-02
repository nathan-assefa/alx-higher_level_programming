const url = 'https://swapi-api.alx-tools.com/api/films/?format=json'

$(() => $.get(url, (data) => {
	const results = data.results
	results.map(result => $('UL#list_movies').append(`<li>${result.title}</li>`))
}))
