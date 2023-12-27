from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os.path
import pickle
import datetime
from googleapiclient.errors import HttpError


# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/calendar.events']

creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'D:\\Projects\\Techfest\\Final\\src\\agents\\Calender\\calenderFunctions\\credentials2.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)



def create_event(start_date_time,end_date_time, title, location=None):
    print("initiating the request")

    service = build("calendar", "v3", credentials=creds)
    event = {
        'summary': title,
        'location': location,
        # 'description':description,
        'start': {
            'dateTime': start_date_time,
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_date_time,
            'timeZone': 'Asia/Kolkata',
        },
    }
    try:
        print("trying the request")

        event = service.events().insert(calendarId="primary", body=event).execute()
        # print(f"event created {event.get('htmlLink')}")
        return True
    except HttpError as error:
        print(f"An error occurred: {error}")
        return False
    
def get_free_slots(start_time, end_time, duration):
    service = build("calendar", "v3", credentials=creds)
    body = {
        "timeMin": start_time,
        "timeMax": end_time,
        "items": [{"id": 'primary'}]
    }
    eventsResult = service.freebusy().query(body=body).execute()
    busy_times = eventsResult[u'calendars'][u'primary'][u'busy']

    # Convert start and end times to datetime objects
    start_time = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%SZ")
    end_time = datetime.datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%SZ")

    # Initialize the current time to the start time
    current_time = start_time

    free_slots = []
    for busy_time in busy_times:
        busy_start = datetime.datetime.strptime(busy_time['start'], "%Y-%m-%dT%H:%M:%SZ")
        busy_end = datetime.datetime.strptime(busy_time['end'], "%Y-%m-%dT%H:%M:%SZ")

        # While there is enough time for a slot before the next busy time
        while current_time + datetime.timedelta(minutes=duration) <= busy_start:
            # Add the slot to the list of free slots
            free_slots.append((current_time, current_time + datetime.timedelta(minutes=duration)))
            # Move the current time to the end of the slot
            current_time += datetime.timedelta(minutes=duration)

        # Move the current time to the end of the busy time
        current_time = busy_end

    # After the last busy time, add all remaining slots to the list of free slots
    while current_time + datetime.timedelta(minutes=duration) <= end_time:
        free_slots.append((current_time, current_time + datetime.timedelta(minutes=duration)))
        current_time += datetime.timedelta(minutes=duration)

    return free_slots