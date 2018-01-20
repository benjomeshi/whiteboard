var bodyParser = require('body-parser');
var fs = require('fs');
var express = require('express');
var app = express();
app.use(bodyParser.urlencoded({extended: true}));
const io = require('socket.io')(8080);
var mysql = require('mysql');

var config_json = JSON.parse(fs.readFileSync('mysql.json', 'utf8'));
var mysql_con;
mysql_con = mysql.createPool({
	host : config_json["host"],
	user : config_json["user"],
	password : config_json["password"],
    database : config_json["db"]}
);

mysql_con.query('SELECT * FROM room;',[], (err, results)=>{
    if (!err) console.log(results); 
});

// app.get(/chat\/[0-9]+/, (req, res) => {
//     console.log(req.url)
//     io
//     .of(req.url)
//     .on('connection', socket => {
//     console.log(`New room: ${req.url}`)
//     socket.emit('hoge') 
//     })
//     res.sendFile(__dirname +'/test_chat.html')
// })

app.post('/room' , (req, res)=>{ 
    console.log(req.body)
    let name = req.body.name
    mysql_con.query("insert into room(name) values(?)", [name], (req, res)=>{})
});

app.listen(3000, () => {
    console.log('Listening on port 3000')
})