#!/usr/bin/node

$(document).ready(() => {
  $('#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
