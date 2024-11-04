from sqlalchemy import create_engine 
import requests
from ApiRes import ApiRes
import warnings
import json 

base_url = 'https://gate.synerget.ru:8179'
api = ApiRes(base_url)
db_connection_string = "postgresql+psycopg2://postgres:postgrespassword@192.168.202.238:5432/postgres"
db = create_engine(db_connection_string)



def test_system_module():
    warnings.filterwarnings('ignore')
    rows = db.execute("select * from system.module where type != 'sts102'").fetchall()
    resp = requests.get(base_url+'/api/data/system/module', headers = api.get_token(), verify = False)
    print(f'len row {len(rows)}')
    print(f'len api {len(resp.json()['data'])}')
    print (f'rows = {rows}')
    print(f'resp = {resp.json()}')

test_system_module()