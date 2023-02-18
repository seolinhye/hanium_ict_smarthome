import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

def checkCredentials(): #creds 파일 확인
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        return False

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def makeCalendar(creds, calendarType="normal"): #구글캘린더 or 공휴일 캘린더 생성
    calendar = build('calendar', 'v3', credentials=creds)
    today = datetime.date.today().isoformat()
    time_min = f'{today}T00:00:00+09:00'
    time_max = f'{today}T23:59:59+09:00'
    max_results = 100
    
    if calendarType=="normal":
        calendar_Id = 'primary'
        schedule = calendar.events().list(calendarId = calendar_Id,timeMin = time_min,
                                        timeMax = time_max,maxResults = max_results ).execute()
    elif calendarType=="holiday":
        calendar_Id = 'ko.south_korea.official#holiday@group.v.calendar.google.com'
        schedule = calendar.events().list(calendarId = calendar_Id, timeMin = time_min,
                                        timeMax = time_max, maxResults = max_results).execute()
    return schedule

def transmissColor(creds): #색조코드 생성
    if creds == False:
        return 0

    schedule = makeCalendar(creds)
    events = schedule.get('items', [])
    colorCode=None
    
    #일정 확인 -> 일정 없으면 공휴일인지 확인 -> 공휴일도 아니면 파란색 출력.
    if events: #summary: 일정명
        print(events[0]["summary"], "Yellow")
        colorCode="Yellow"
        
    schedule = makeCalendar(creds,"holiday")
    holidays = schedule.get('items', [])
    if holidays:
        print(holidays[0]["summary"],"Red")
        colorCode="Red"
        
    if not colorCode:
        print("평범한 하루","Blue")
        colorCode="Blue"
    return colorCode

