import requests
from requests.auth import HTTPBasicAuth
import os
import base64
import pickle
import google.auth
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import email
import re

class github_apis:
    def __init__(self, username, token):
        self.username = username
        self.token = token
    
    def req_pull(self,repo_owner,repo_name):
        self.url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/1'
        self.headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        self.response = requests.get(self.url, headers= self.headers)
        if self.response.status_code == 200:
            pull_requests = self.response.json()
            print(f"PR #{pull_requests['number']} - {pull_requests['title']} by {pull_requests['user']['login']}")
        else:
            print(f"Failed to fetch pull requests. Status code: {self.response.status_code}")

    def req_issues(self,repo_owner,repo_name):
        self.url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues'
        self.headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        self.response = requests.get(self.url, headers= self.headers)
        if self.response.status_code == 200:
            self.issues = self.response.json()
            for issue in self.issues:
                print(type(issue))
                print(f"issue #{issue['number']} - {issue['title']} by {issue['user']['login']}")
        else:
            print(f"Failed to fetch pull requests. Status code: {self.response.status_code}")


class gmail_api:
    def get_service():
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        SCOPES = ['https://www.googleapis.com/auth/gmail.send']
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('gmail', 'v1', credentials=creds)
        return service
    
    def create_message(sender, to, subject, message_text):
        """Create a message for an email."""
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
    
    def send_message(service, user_id, message):
        """Send an email message."""
        try:
            message = (service.users().messages().send(userId=user_id, body=message)
                    .execute())
            print('Message Id: %s' % message['id'])
            return message
        except Exception as error:
            print('An error occurred: %s' % error)
            return None
        
    def list_messages(service, user_id, query=''):
        """List all Messages of the user's mailbox matching the query."""
        try:
            response = service.users().messages().list(userId=user_id, q=query).execute()
            messages = []
            if 'messages' in response:
                messages.extend(response['messages'])

            while 'nextPageToken' in response:
                page_token = response['nextPageToken']
                response = service.users().messages().list(userId=user_id, q=query, pageToken=page_token).execute()
                messages.extend(response['messages'])

            return messages
        except Exception as error:
            print('An error occurred: %s' % error)
            return None
        
    def get_message(service, user_id, msg_id):
        """Get a Message with given ID."""
        try:
            message = service.users().messages().get(userId=user_id, id=msg_id).execute()
            return message
        except Exception as error:
            print('An error occurred: %s' % error)
            return None 
    
    def get_mime_message(service, user_id, msg_id):
        """Get a Message and use it to create a MIME Message."""
        try:
            message = service.users().messages().get(userId=user_id, id=msg_id, format='raw').execute()
            msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))
            mime_msg = email.message_from_bytes(msg_str)
            return mime_msg
        except Exception as error:
            print('An error occurred: %s' % error)
            return None
        
    def print_message(self,service, user_id, msg_id):
        """Prints the details of a specific email message."""
        message = self.get_message(service, user_id, msg_id)
        if message:
            headers = message['payload']['headers']
            for header in headers:
                if header['name'] == 'Subject':
                    subject = header['value']
                if header['name'] == 'From':
                    sender = header['value']
            print(f'Subject: {subject}')
            print(f'From: {sender}')
            print('Message snippet:')
            print(message['snippet'])



def main():
    api = github_apis("devHarshShah","your token")
    api.req_issues("sarveshdakhore","papyrus")

    mail = gmail_api()
    service = mail.get_service()
    sender = "your-email@gmail.com"
    to = "recipient-email@gmail.com"
    subject = "Test Email"
    message_text = "This is a test email sent using the Gmail API"
    
    message = mail.create_message(sender, to, subject, message_text)
    mail.send_message(service, 'me', message)


    user_id = 'me'
    query = 'is:unread'  # Modify the query as needed
    messages = mail.list_messages(service, user_id, query)

    if messages:
        print(f'Found {len(messages)} unread messages.')
        for message in messages:
            mail.print_message(service, user_id, message['id'])
    else:
        print('No unread messages found.')

if __name__ == "__main__":
    main()