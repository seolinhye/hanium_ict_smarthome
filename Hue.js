//전구 제어
function getID(client){
    return new Promise((resolve)=>{
        client.devices.list().then(devices => {

            for (const i in devices){
                if(devices[i].components[0].categories[0].name == 'Light'){
                     hueID = devices[i].deviceId
                     resolve(hueID)
                }
            }
        })
    });   
}


var hueON = function(){
    client = global.client
    promise1 = getID(client)
    promise1.then((value) => {
        client.devices.executeCommands(value,[{'capability':'switch', 'command':'on'}]).then(device => 
            {console.log(device)})})
}

var hueOFF = function(){
    client = global.client
    promise1 = getID(client)
    promise1.then((value) => {
        client.devices.executeCommands(value,[{'capability':'switch', 'command':'off'}]).then(device => 
            {console.log(device)})})
}

var hueRED = function(){
    client = global.client
    promise1 = getID(client)
    promise1.then((value) => {
        
        client.devices.executeCommands(value,[{'capability':'switch', 'command':'on'},{'capability':'colorControl','command':"setColor",'arguments':[{'hue':3, 'saturation':100}]}]).then(device => 
            {console.log(device)})})
}

var hueBLUE = function(){
    client = global.client
    promise1 = getID(client)
    promise1.then((value) => {
        client.devices.executeCommands(value,[{'capability':'switch', 'command':'on'},{'capability':'colorControl','command':"setColor",'arguments':[{'hue':69.32, 'saturation':100}]}]).then(device => 
            {console.log(device)})})
}

var hueYELLOW = function(){
    client = global.client
    promise1 = getID(client)
    
    promise1.then((value) => {
        client.devices.executeCommands(value,[{'capability':'switch', 'command':'on'},{'capability':'colorControl','command':"setColor",'arguments':[{'hue':16.48, 'saturation':100}]}]).then(device => 
            {console.log(device)})})
}

module.exports = {
    hueOFF,
    hueON,
    hueRED,
    hueYELLOW,
    hueBLUE,
}
