import requests, json
from urllib.request import urlopen
from time import sleep
# https://developers.meethue.com/develop/get-started-2/

bridge_IP=''
while(True):
    try: # HTTP 419 오류 발생 시 수동입력
        bridgeData_IP = requests.get("https://discovery.meethue.com").json()
        print(bridgeData_IP)
        bridge_IP=bridgeData_IP[0]["internalipaddress"]
    except:
        bridge_IP=input("브릿지의 IP를 수동 입력해주세요: ") 
        
    else:
        if requests.get(f"https://{bridge_IP}/api/newdeveloper",verify=False).status_code==200:
            break
        
while(True): 
    #안전하지 않은 페이지 처리 verify=False
    bridgeData = requests.post(f"https://{bridge_IP}/api",verify=False ,json={"devicetype":"my_hue_app#iphone peter"})
    
    #HTTP 200 정상 요청
    if bridgeData.status_code== 200:      
        bridgeJsonData=bridgeData.json()
        #브릿지의 버튼이 눌렸을때
        if bridgeJsonData[0].get("success"): 
            id_dict=bridgeJsonData[0].get("success")
            user_name = id_dict["username"]
            print("user_name 저장 완료")
            break
        print("브릿지의 버튼을 눌러주세요!")
        
    #url 오류
    else:
        print("URL 확인 요망")

    sleep(2)

url=f'http://{bridge_IP}/api/{user_name}/lights'
requestData = requests.get(url)
#최종 API 주소
print(url)

#HTTP 200 정상 요청
if requestData.status_code== 200:      
    jsonData=requestData.json()
    print(jsonData)
    
#url 오류
else:
    print("URL 확인 요망")

#bri : 밝기(0~254), sat: 채도(0~254), Hue: 색조값(0~65535)
if jsonData:
    command = input("Power(전원), Color(색조), Sat(채도), Bri(밝기) 중 입력: ")
    if command == "Power":
        power = input("On / OFF : ")
        if power == "On":
            requests.put(url+'/1/state',json={"on": True})
        if power == "Off":
            requests.put(url+'/1/state',json={"on": False})
            
    elif command == "Color":
        color = input("Red / Yellow / Blue : ")
        if color == "Red":
            requests.put(url+'/1/state',json={'hue': 176})
        elif color == "Yellow":
            requests.put(url+'/1/state',json={'hue': 10819})
        elif color == "Blue":
            requests.put(url+'/1/state',json={'hue': 43969})
            
    elif command == "Sat":
        sat= int(input("채도(0~254): "))
        if 0<=sat<=254:
            requests.put(url+'/1/state',json={'sat': sat})
            
    elif command == "Bri":
        bri= int(input("밝기(0~254): "))
        if 0<=bri<=254:
            requests.put(url+'/1/state',json={'bri': bri}) 
    else:
        print("오타 발생")
