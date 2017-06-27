'''

- Create virtualenv
- activate virtual env
- pip install --upgrade oauth2client
- python service_account.py

'''
from oauth2client.service_account import ServiceAccountCredentials
import httplib2

def main():
    scopes = ['https://www.googleapis.com/auth/devstorage.read_write']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('[replace with your service account file.json]', scopes)
    http = httplib2.Http()
    credentials.refresh(http)
    print credentials.access_token

if __name__ == '__main__':
    main()
