import requests, bs4
from urllib.request import Request
from urllib.parse import urlencode, unquote
import datetime

def getTH_API(serviceKey):
    
    response = requests.get(makeURL(serviceKey)).text.encode('utf-8') 
    xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')                   
    if xmlobj.response.header.resultCode.text=="01":
        response = requests.get(makeURL(serviceKey,"01")).text.encode('utf-8') 
        xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')                 
    return xmlobj

def makeURL(serviceKey, errorcode="00"): #가끔 **시00분에 API가 바로 업로드 되지 않았을때 에러 발생
    xmlUrl = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    today = datetime.datetime.now()
    baseTime="0000"
    if errorcode=="00":
        baseTime=today.strftime("%H")+"00"
    elif errorcode=="01":
        hour = datetime.timedelta(hours = 1)
        baseTime=(today-hour).strftime("%H")+"00"
    
    queryParams = '?' + urlencode(
            {
                'ServiceKey' : serviceKey,    
                'pageNo'     : '1',          
                'numOfRows'  : '10', 
                'dataType'   : 'XML',                      # 요청자료형식(XML/JSON)
                'base_date'  : today.strftime("%Y%m%d"),   # 현재날짜
                'base_time'  : baseTime,                   # 현재시간(정시단위) 매시각 40분 이후 호출 (가끔 오류 발생 원인) 
                'nx'         : '59',                       # 예보지점의 X 좌표값
                'ny'         : '125'                       # 예보지점의 Y 좌표값 (현재 동작구로 설정)        
            }
        )
    return xmlUrl + queryParams
        
def getTempHumid(xml):
    TempHumid={}
    for Item in xml.findAll('item'):
        if Item.category.text=="REH":
            TempHumid["Humid"]=Item.obsrValue.text
        elif Item.category.text=="T1H":
            TempHumid["Temp"]=Item.obsrValue.text
    return TempHumid
