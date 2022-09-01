from lib2to3.pgen2 import token
import requests

token_endpoint = 'http://localhost:8000/api/authtoken/'
endpoint = 'http://localhost:8000/api/product/'

data = {
        'title':'sun',
        'content':'womeo',
        'price':72
}

get_response = requests.get(endpoint)
'''
if get_response.status_code == 403:
        get_token = requests.post(token_endpoint, json={'username':'ljt123', 'password':'L123789.'})
        # print()
        auth_token = get_token.json()['token']
        # auth_token = 'c6f8c160a98844e01246823a44cb153dfb65833b'
        headers = {
                'Authorization' : f'Token {auth_token}'
        }
        get_response = requests.get(endpoint, headers=headers)
'''
print(get_response.json())
print(get_response.status_code)

 