#!/usr/bin/node
$(function () {
  $(document).ready(function sayHello () {
    $.get('https://stefanbohacek.com/hellosalut/?lang=fr', (data) => {
      const hello = data.hello;
      $('DIV#hello').text(hello);
    });
  });
});
