import requests
from ast import literal_eval

class Authenticate(object):

    def __init__(self):
        super().__init__()

    def authentication(self):
        '''
        Hits Authentication endpoint and gets Session Token, access ID and access Key
        are generated in Cedato platform. API Key must be base64 encoded, format is encoded AccessKey:Secret
        '''

        payload = {'grant_type': 'client_credentials'}
        header = {
            'accept': 'application/json',
            'api-version': '1',
            'authorization': 'Basic {0}', # insert your base64 encrypted AccessKey:Secret here
            'content-type': 'application/x-www-form-urlencoded'
        }
        session_url = 'https://api.cedato.com/api/token'
        response = requests.post(session_url, data=payload, headers=header)
        token = literal_eval(response.text)['data']['access_token']
        return token
