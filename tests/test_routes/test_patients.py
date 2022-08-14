import requests
from utils import get_header, URL

PATH = 'v1/patients'
ENDPOINT = f'{URL}{PATH}'


def test_patients():
    r = requests.get(ENDPOINT, headers=get_header())
    assert r.status_code == 200
