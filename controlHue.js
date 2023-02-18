const {SmartThingsClient, BearerTokenAuthenticator} = require('@smartthings/core-sdk')
const client = new SmartThingsClient(new BearerTokenAuthenticator('PAT'))

function getID(){
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


function hueON(){
    promise1 = getID()
    promise1.then((value)=> {
        client.devices.executeCommands(value,[{'capability':'switch', 'command':'on'}]).then(device=>{console.log(device)})
    })
}
function hueOFF(){
    promise1 = getID()
    promise1.then((value)=> {
        client.devices.executeCommands(value,[{'capability':'switch', 'command':'off'}]).then(device=>{console.log(device)})
    })
}
function hueRED(){
    promise1 = getID()
    promise1.then((value)=> {
        client.devices.executeCommands(value,[{'capability':'colorControl','command':"setColor",'arguments':[{'hue':3, 'saturation':100}]}]).then(device=>{console.log(device)})
    })
}