var bodyParser = require('body-parser');
var fs = require('fs');
var express = require('express');
var passwordHash = require('password-hash');
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

app.post('/user', (req, res)=>{
    console.log(req.body)
    let name = req.body.name
    let username = req.body.username
    let password = passwordHash.generate(req.body.password)
    mysql_con.query("insert into user(name, username, password) values(?,?,?)", [name, username, password], (err, result)=>{
        if(err){console.log("Insert error!")}else{console.log("Success")}
    });
});

app.post('/room' , (req, res)=>{ 
    console.log(req.body)
    let name = req.body.name
    let password = req.body.password
    mysql_con.query("insert into room(name, password) values(?,?)", [name,password], (req, res)=>{
        if(err){console.log("Insert error!")}
    });
});

app.get('/user', (req, res)=>{
    mysql_con.query('SELECT name FROM user;',[], (err, results)=>{
        if (!err) res.send(results)
    });
});

app.get('/room', (req, res)=>{
    mysql_con.query('SELECT id, name FROM room;',[], (err, results)=>{
        if (!err) res.send(results)
    });
});

app.listen(3000, () => {
    console.log('Listening on port 3000')
})