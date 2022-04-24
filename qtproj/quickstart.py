from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    cred_dict = {"installed": {"client_id": "743839589694-qnqdhqm799g46ubvqs86b5kc5igvpuqf.apps.googleusercontent.com",
                               "project_id": "base-api-306807", "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                               "token_uri": "https://oauth2.googleapis.com/token",
                               "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                               "client_secret": "yTbP19CqCfro6y4pBDfIMMnK",
                               "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"],
                               "refresh_token": None}}

    creds = Credentials.from_authorized_user_info(cred_dict["installed"])
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config(cred_dict, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])


if __name__ == '__main__':
    main()
