import requests
from utils import get_header, URL

PATH = 'v1/transactions'
ENDPOINT = f'{URL}{PATH}'


def test_transactions():
    r = requests.get(ENDPOINT, headers=get_header())
    assert r.status_code == 200


def test_transactions_filter_patientname():
    PATIENT_NAME = "abraao"
    header = get_header()
    params = {"PATIENT_NAME": PATIENT_NAME}
    r = requests.get(ENDPOINT, headers=header, params=params)
    body = r.json()
    assert r.status_code == 200
    assert all(map(lambda x: PATIENT_NAME.lower() in (x["PATIENT_FIRST_NAME"] + x["PATIENT_LAST_NAME"]).lower(), body))


def test_transactions_filter_pharmacyname():
    PHARMACY_NAME = "drogasil"
    header = get_header()
    params = {"PHARMACY_NAME": PHARMACY_NAME}
    r = requests.get(ENDPOINT, headers=header, params=params)
    body = r.json()
    assert r.status_code == 200
    assert all(map(lambda x: PHARMACY_NAME.lower() in x["PHARMACY_NAME"].lower(), body))

def test_transactions_filter_pharmacycity():
    PHARMACY_CITY = "paulo"
    header = get_header()
    params = {"PHARMACY_CITY": PHARMACY_CITY}
    r = requests.get(ENDPOINT, headers=header, params=params)
    body = r.json()
    assert r.status_code == 200
    assert all(map(lambda x: PHARMACY_CITY.lower() in x["PHARMACY_CITY"].lower(), body))
