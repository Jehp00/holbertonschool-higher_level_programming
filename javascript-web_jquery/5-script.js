#!/usr/bin/node
$(function () {
  $('DIV#add_item').click(function () {
    $('ul.my_list').append($('<li></li>').text('Item'));
  });
});
