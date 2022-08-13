import requests
from utils import get_header


def test_pharmacies():
    r = requests.get('http://127.0.0.1:8000/v1/pharmacies', headers=get_header())
    assert r.status_code == 200
