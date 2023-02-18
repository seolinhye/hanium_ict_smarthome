from collections import defaultdict
from urllib.parse import quote_plus, urlencode
import numpy as np
import pandas as pd
import requests
import xmltodict

def getSName(umd,serviceKey):
  #FIND your tmX,tmY
  api = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getTMStdrCrdnt'

  queryParams = '?' + urlencode({quote_plus('numOfRows'): '1000',
                                 quote_plus('pageNo'): '1',
                                 quote_plus('umdName'): umd,
                                 quote_plus('returnType'): 'xml',
                                 quote_plus('serviceKey'): serviceKey
                                 })
  
  url = api+queryParams
  res = requests.get(url).content
  xml = xmltodict.parse(res)
  dict_data = xml['response']['body']['items']['item']
  df = pd.DataFrame(dict_data)
  tmp = df.iloc[:,[0,1,4]]
  tmp.index = tmp.index + 1
  #print(tmp)

  num =  1 # input('Choose your Address: ') 

  tmX = df.iat[int(num)-1,2]
  tmY = df.iat[int(num)-1,3]


  #FIND StationName
  api = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getNearbyMsrstnList'

  queryParams = '?' + urlencode({quote_plus('numOfRows'): '1000',
                                 quote_plus('pageNo'): '1',
                                 quote_plus('tmX'): tmX,
                                 quote_plus('tmY'): tmY,
                                 quote_plus('returnType'): 'xml',
                                 quote_plus('serviceKey'): '0KvAF1fy+e0EQYpAjLmz5Am/g+1+LwNY1GpDZj8a6BdW+FSz9UTVNtiWF4CYC5nbkUKiaJjZw7Pnl6Su6HKh4A==' #serviceKey
                                })
      
  url = api+queryParams
  res = requests.get(url).content
  xml = xmltodict.parse(res)
  dict_data = xml['response']['body']['items']['item']
  df = pd.DataFrame(dict_data)
  df = df.sort_values(by=['tm'], axis=0)
  StationName = df.iat[0,2]
  #print (StationName)

  return StationName


def getDust_API(StationName,serviceKey):
  #FIND dust info
  api = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'

  queryParams = '?' + urlencode({quote_plus('numOfRows'): '1000',
                                 quote_plus('pageNo'): '1',
                                 quote_plus('stationName'): StationName,
                                 quote_plus('dataTerm'): 'DAILY',
                                 quote_plus('ver'): '1.3',
                                 quote_plus('returnType'): 'xml',
                                 quote_plus('serviceKey'): serviceKey
                                 })
      
  url = api+queryParams
  res = requests.get(url).content
  xml = xmltodict.parse(res)
  dict_data = xml['response']['body']['items']['item']
  df = pd.DataFrame(dict_data)
  
  #Real-time DUST 
  pm10 = df.iat[0,5]
  pm25 = df.iat[0,8]
  #print('pm10: ',pm10)
  #print('pm25: ',pm25)

  return [pm10,pm25]


def getDustG_API(StationName,serviceKey):
  #FIND dust info
  api = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'

  queryParams = '?' + urlencode({quote_plus('numOfRows'): '1000',
                                quote_plus('pageNo'): '1',
                                quote_plus('stationName'): StationName,
                                quote_plus('dataTerm'): 'DAILY',
                                quote_plus('ver'): '1.3',
                                quote_plus('returnType'): 'xml',
                                quote_plus('serviceKey'): serviceKey
                                })
      
  url = api+queryParams
  res = requests.get(url).content
  xml = xmltodict.parse(res)
  dict_data = xml['response']['body']['items']['item']
  df = pd.DataFrame(dict_data)

  #Real-time DUST GRADE
  df_dustG = df.loc[[0],['pm10Grade1h','pm25Grade1h']] 

  for i in range(0,2):
    tmp = df_dustG.iat[0,int(i)]

    if i ==0:
      if tmp == '1':
        G10 = ("good ")
      elif tmp == '2':
        G10 = ("soso")
      elif tmp == '3':
        G10 = ("bad")
      else:
        G10 = ("very bad")

    else:
      if tmp == '1':
        G25 = ("good ")
      elif tmp == '2':
        G25 = ("soso")
      elif tmp == '3':
        G25 = ("bad")
      else:
        G25 = ("very bad")


  #print(G10,G25)
  #print(df_dustG)
  return [G10,G25]

import sys

if __name__ == '__main__':
  SN = getSName(sys.argv[1], sys.argv[2])

  dustV = getDust_API(SN, sys.argv[2])
  
  dustG = getDustG_API(SN, sys.argv[2])

  #print(dustV)

  #print(dustG)

  argu = [dustV[0],dustV[1], dustG[0],dustG[1]]
  #print(argu)