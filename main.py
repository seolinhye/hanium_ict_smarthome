#pip install schedule
import time
import requests
import schedule
from openapi.weather import DUST as dust
from openapi.calendar import API_Calendar as cal

def job():
    #dust value 받아오기
    print(dust.getDust_API('종로구',serviceKey))
    print(dust.getDustG_API('종로구',serviceKey))

schedule.every().hour.at(":05").do(job) #openAPI갱신되는 시간 고려해서 매 시간 05분마다 반복

schedule.every(5).seconds.do(job) #test용 print
color = cal.transmissColor(cal.checkCredentials())

if color == 0:
    print("no token")
elif color == "Yellow":
    requests.get("http://localhost:3000/hueYELLOW")

elif color == "Blue":
    requests.get("http://localhost:3000/hueBLUE")

elif color == "Red":
    requests.get("http://localhost:3000/hueRED")

while True:
    schedule.run_pending()
    time.sleep(1)

