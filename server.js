var ap = require('./air.js');
var ac = require('./ac.js');
var hue = require('./hue.js');

const {SmartThingsClient, BearerTokenAuthenticator} = require('@smartthings/core-sdk')
const express = require('express');
const {spawn} = require('child_process');
const { mainModule } = require('process');
const { response } = require('express');
var url = require('url');
const server = express()



//PAT
server.get('/setPAT', (req, res) => {
    global.client = new SmartThingsClient(new BearerTokenAuthenticator(req.query.PAT))
    res.send("good")
});




server.get('/', function(req,res){
    res.sendFile(__dirname + '/public/main.html');
});

server.get('/apON', (req, res) => {
    ap.apON();
    res.send('AirPurifier is ON')
});

server.get('/apOFF', (req, res) => {
    ap.apOFF();
    res.send('AirPurifier is OFF')
});

server.get('/apSleepON', (req, res) => {
    ap.apSleepON();
    res.send('AirPurifier sleep mode is ON')
});

server.get('/apSleepOFF', (req, res) => {
    ap.apSleepOFF();
    res.send('AirPurifier sleep mode is OFF')
});

server.listen(3000, function(){
    console.log('EXPRESS start on port 3000');
});

server.get('/acON', (req, res) => {
    ac.acON();
});

server.get('/acOFF', (req, res) => {
    ac.acOFF();
});

server.get('/acChangeTemp', (req, res) => {
    ac.acChangeTemp(req.query.temp);
});

server.get('/acCoolMode', (req, res) => {
    ac.acCoolMode();
});

server.get('/acDryMode', (req, res) => {
    ac.acDryMode();
});

server.get('/acNowTemp', (req, res) => {
    temp = ac.acNowTemp();
    response.writeHead(200, {'Content-Type':'text/html'});
    response.write('<h1><%= temp %></h1>')
    response.end('');
});

//hue
server.get('/hueOFF', (req, res) => {
    hue.hueOFF();
    res.send("good")
});

server.get('/hueON', (req, res) => {
    hue.hueON();
    res.send("good")
});

server.get('/hueRED', (req, res) => {
    hue.hueRED();
    res.send("good")
});

server.get('/hueYELLOW', (req, res) => {
   
    hue.hueYELLOW();
    res.send("good")
});

server.get('/hueBLUE', (req, res) => {
    hue.hueBLUE();
    res.send("good")
});