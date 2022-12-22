#!/usr/bin/node
$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (resp, status) {
    if (status === 'success') {
      const films = resp.results;
      for (const i in films) {
        $('#list_movies').append('<li>' + films[i].title + '</li>');
      }
    }
  });
});
