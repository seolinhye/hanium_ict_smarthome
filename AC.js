//에어컨 제어
function getID(client){
    return new Promise((resolve, reject)=>{
        client.devices.list().then(devices => {

            for (const i in devices){
                if(devices[i].components[0].categories[0].name == 'AirConditioner'){
                     acID = devices[i].deviceId
                     resolve(acID)
                }
            }
        })
    });   
}

var acON = function(){
    client = global.client
    promise1 = getID(client)
    promise1.then((value) => {
         client.devices.executeCommands(value,[{'capability':'switch', 'command':'on'}]).then(device => 
            {console.log(device)})})
}

var acOFF = function(){
    client = global.client
    promise1 = getID(client)
    promise1.then((value) => {
        client.devices.executeCommands(value,[{'capability':'switch', 'command':'off'}]).then(device => 
            {console.log(device)})})
}

var acChangeTemp = function(temp){
    client = global.client
    promise1 = getID(client)
    promise1.then((value) => {
        client.devices.executeCommands(value,[{'capability':'thermostatCoolingSetpoint','command':"setCoolingSetpoint",'arguments':[parseInt(temp)]}]).then(device => 
            {console.log(device)})})
}
var acDryMode = function(){
    client = global.client
    promise1 = getID(client)
    promise1.then((value) => {
        client.devices.executeCommands(value,[{'capability':'airConditionerMode','command':"setAirConditionerMode",'arguments':['dry']}]).then(device => 
            {console.log(device)})})
}
var acCoolMode = function(){
    client = global.client
    promise1 = getID(client)
    promise1.then((value) => {
        client.devices.executeCommands(value,[{'capability':'airConditionerMode','command':"setAirConditionerMode",'arguments':['cool']}]).then(device => 
            {console.log(device)})})
}
var acNowTemp = function(){
    client = global.client
    promise1 = getID(client)
    promise1.then((value) => {
        client.devices.getCapabilityStatus(value,'main',"temperatureMeasurement").then(device=>{console.log(device.temperature.value)})})
    return device.temperature.value
}


module.exports = {
    acON,
    acOFF,
    acChangeTemp,
    acCoolMode,
    acDryMode,
    acNowTemp
}
