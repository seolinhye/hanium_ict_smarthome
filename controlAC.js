const {SmartThingsClient, BearerTokenAuthenticator} = require('@smartthings/core-sdk')
const client = new SmartThingsClient(new BearerTokenAuthenticator('PAT'))

function getID(){
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

function acOFF(){
    promise1 = getID()
    promise1.then((value)=> {
        client.devices.executeCommands(value,[{'capability':'switch', 'command':'off'}]).then(device=>{console.log(device)})
    })
}
function acON(){
    promise1 = getID()
    promise1.then((value)=> {
        client.devices.executeCommands(value,[{'capability':'switch', 'command':'on'}]).then(device=>{console.log(device)})
    })
}
function acChangeTemp(){
    promise1 = getID()
    promise1.then((value)=> {
        client.devices.executeCommands(value,[{'capability':'thermostatCoolingSetpoint','command':"setCoolingSetpoint",'arguments':[26]}]).then(device=>{console.log(device)})
    })
}
function acNowTemp(){
    promise1 = getID()
    promise1.then((value)=> {
        client.devices.getCapabilityStatus(value,'main',"temperatureMeasurement").then(device=>{console.log(device.temperature.value)})
    })
}
function acDryMode(){
    promise1 = getID()
    promise1.then((value)=> {
        client.devices.executeCommands(value,[{'capability':'airConditionerMode','command':"setAirConditionerMode",'arguments':['dry']}]).then(device=>{console.log(device)})
    })
}
function acCoolMode(){
    promise1 = getID()
    promise1.then((value)=> {
        client.devices.executeCommands(value,[{'capability':'airConditionerMode','command':"setAirConditionerMode",'arguments':['cool']}]).then(device=>{console.log(device)})
    })
}
