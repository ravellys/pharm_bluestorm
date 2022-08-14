import requests

URL = 'http://127.0.0.1:8000/'
USERNAME = 'teste'
PASSWORD = 'teste'


def get_login_token():
    body = {
        'username': USERNAME,
        'password': PASSWORD
    }
    r = requests.post(f'{URL}v1/login/token', data=body)
    return r.json()


def get_header():
    token = get_login_token()
    header = {
        'accept': 'application/json',
        'Authorization': f'{token["token_type"].capitalize()} {token["access_token"]}'
    }
    return header


if __name__ == '__main__':
    print(get_header())
