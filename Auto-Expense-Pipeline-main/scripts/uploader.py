import os
import pickle
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/drive.file']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLIENT_SECRET_FILE = os.path.join(BASE_DIR, "configs", "client_secret.json")
TOKEN_FILE = os.path.join(BASE_DIR, "configs", "token.pickle")

def get_credentials():
    creds = None

   
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)

    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES
            )
            creds = flow.run_local_server(port=0)

        
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    return creds


def upload_to_drive(file_path):
    try:
        creds = get_credentials()
        service = build('drive', 'v3', credentials=creds)

        FOLDER_ID = "1dq_ZhF9zyToRBtirtB4zLe4L59EpVJuD"

        file_metadata = {
            'name': os.path.basename(file_path),
            'parents': [FOLDER_ID]   
        }

        media = MediaFileUpload(file_path)

        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()

        print("Uploaded successfully. File ID:", file.get('id'))

    except Exception as e:
        print("Upload failed:", e)
