"""
Shows basic usage of the Apps Script API.
Call the Apps Script API to create a new script project, upload a file to the
project, and log the script's URL to the user.
"""

import os.path

from os.path import join as pjoin
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import errors
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/script.projects',
          'https://www.googleapis.com/auth/script.external_request']

SAMPLE_CODE = '''
function buildCard() {
    cardSection1DecoratedText1Icon1 = CardService.newIconImage()
        .setIconUrl(
            'https://koolinus.files.wordpress.com/2019/03/avataaars-e28093-koolinus-1-12mar2019.png'
        );

    cardSection1DecoratedText1 = CardService.newDecoratedText()
        .setText('John Doe')
        .setBottomLabel('Software engineer')
        .setStartIcon(cardSection1DecoratedText1Icon1);

    cardSection1DecoratedText2Icon1 = CardService.newIconImage()
        .setIconUrl(
            'https://happyfacesparty.com/wp-content/uploads/2019/06/avataaars-Brittany.png'
        );

    cardSection1DecoratedText2 = CardService.newDecoratedText()
        .setText('Jane Doe')
        .setBottomLabel('Product manager')
        .setStartIcon(cardSection1DecoratedText2Icon1);

    cardSection1DecoratedText3Icon1 = CardService.newIconImage()
        .setIconUrl(
            'https://i2.wp.com/tunisaid.org/wp-content/uploads/2019/03/avataaars-2.png?ssl=1'
        );

    cardSection1DecoratedText3 = CardService.newDecoratedText()
        .setText('Jamie Doe')
        .setBottomLabel('Vice president')
        .setStartIcon(cardSection1DecoratedText3Icon1);

    cardSection1 = CardService.newCardSection()
        .setHeader('List of users')
        .addWidget(cardSection1DecoratedText1)
        .addWidget(cardSection1DecoratedText2)
        .addWidget(cardSection1DecoratedText3);

    card = CardService.newCardBuilder()
        .addSection(cardSection1)
        .build();
    return card;
}
'''.strip()

SAMPLE_MANIFEST = '''
{
  "timeZone": "America/New_York",
  "exceptionLogging": "CLOUD"
}
'''.strip()


API_KEY = "AIzaSyBBa71awj4wiILQiKBkpgtOlgPd7gNKTUU"
PATH = "/Users/skoudoro/devel/futzs/cardservice/tests"

def main():
    """Calls the Apps Script API.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(pjoin(PATH, 'token.json')):
        creds = Credentials.from_authorized_user_file(pjoin(PATH, 'token.json'),
                                                     SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                pjoin(PATH, 'credentials.json'), SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(pjoin(PATH, 'token.json'), 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('script', 'v1', credentials=creds)

        # Call the Apps Script API
        # Create a new project
        request = {'title': 'My Script'}
        response = service.projects().create(body=request).execute()

        # Upload two files to the project
        request = {
            'files': [{
                'name': 'hello',
                'type': 'SERVER_JS',
                'source': SAMPLE_CODE
            }, {
                'name': 'appsscript',
                'type': 'JSON',
                'source': SAMPLE_MANIFEST
            }]
        }
        response = service.projects().updateContent(
            body=request,
            scriptId=response['scriptId']).execute()
        print(response)
        # import ipdb; ipdb.set_trace()
        print('https://script.google.com/d/' + response['scriptId'] + '/edit')

        request = {"function": "buildCard"}
        response = service.scripts().run(scriptId=response['scriptId'],
                                         body=request).execute()
        folder_set = response['response'].get('result', {})
        print(folder_set)

    except errors.HttpError as error:
        # The API encountered a problem.
        print(error.content)


if __name__ == '__main__':
    main()