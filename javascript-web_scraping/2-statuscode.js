#!/usr/bin/node
const args = process.argv.slice(2)
const link = args[0];
const request = require('request');
request(link, (error, response, body) => {
    if (error) {
        console.error('error:', error);
    }
    console.log('code:', response && response.statusCode);
});