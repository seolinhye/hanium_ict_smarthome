//공기청정기 제어
function getID(client){
    return new Promise((resolve, reject)=> {
        client.devices.list().then(devices => {

            for (const i in devices){
                if(devices[i].components[0].categories[0].name == 'AirPurifier'){
                     apID = devices[i].deviceId
                     resolve(apID)
                }
            }
        })
    })   
}

var apON = function(){
    client = global.client
    promise1 = getID(client)
    promise1.then((value) => {
        client.devices.executeCommands(value,[{'capability':'switch','command':'on','component':'main','arguments':[]}]).then(device => 
            {console.log(device)})})
}

var apOFF = function(){
    client = global.client
    promise1 = getID(client)
    promise1.then((value) => {
        client.devices.executeCommands(value,[{'capability':'switch','command':'off','component':'main','arguments':[]}]).then(device => 
            {console.log(device)})})
}

var apSleepON = function(){
    client = global.client
    promise1 = getID(client)
    promise1.then((value) => {
        client.devices.executeCommands(value,[{'capability':'airConditionerFanMode','command':'setFanMode','component':'main','arguments':['sleep']}]).then(device => 
            {console.log(device)})})
}

var apSleepOFF = function(){
    client = global.client
    promise1 = getID(client)
    promise1.then((value) => {
        client.devices.executeCommands(value,[{'capability':'airConditionerFanMode','command':'setFanMode','component':'main','arguments':['auto']}]).then(device => 
            {console.log(device)})})
}

module.exports = {
    apON,
    apOFF,
    apSleepON,
    apSleepOFF
}


