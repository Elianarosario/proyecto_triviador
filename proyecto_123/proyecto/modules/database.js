var mysql = require('mysql');

var connection = mysql.createConnection({
   host: 'localhost',
   user: 'trivial_sem',
   password: 'trivial_sem',
   database: 'trivial_sem'
});