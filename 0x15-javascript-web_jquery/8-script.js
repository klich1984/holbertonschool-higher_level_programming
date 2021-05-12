#!/usr/bin/node

$(document).ready(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
    for (let idx = 0; idx < data.results.length; idx++){
      $('#list_movies').append('<li>' + data.results[idx].title) + '</li>';
    }
  });
});
