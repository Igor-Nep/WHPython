import requests
import json
base_url = 'https://x-clients-be.onrender.com'
def test_requests():
    resp = requests.get(base_url+'/company')
    response_body = resp.json()
    first_com = response_body[0]
    assert first_com["name"] == "Барбершоп 'ЦирюльникЪ'"
    

def test_auth():
    creds = {       
    'username': 'michaelangelo',
    'password': 'party-dude'
    }
    resp = requests.post(base_url+'/auth/login', json=creds)
    token = resp.json()["userToken"]
    assert resp.status_code == 201    
    
def test_create_com():
    creds = {       
    'username': 'raphael',
    'password': 'cool-but-crude'
    }

    company = {       
    'name': 'INEP',
    'description': 'Nemov Co'
    }
    #авторизация
    resp = requests.post(base_url+'/auth/login', json=creds)
    token = resp.json()["userToken"]
    #создание
    my_headers = {}
    my_headers["x-client-token"] = token  
    
    create = requests.post(base_url+'/company', json=company, headers=my_headers)
    assert create.status_code == 201
