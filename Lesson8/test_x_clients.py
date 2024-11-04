import requests
import json
from CompanyApi import CompanyApi

api = CompanyApi('https://x-clients-be.onrender.com')




def test_get_companies():
    body = api.get_company_list()
    assert len(body) > 0

def test_get_active_companies():
    #список всех компаний
    #список активных компаний
    #проверить список 1Ю2

    full_list = api.get_company_list()
    my_params ={
        'active': 'true'
    }
    resp = requests.get('https://x-clients-be.onrender.com'+'/company', params=my_params)
    filtred_list = resp.json()
    
    assert len(full_list) > len(filtred_list)

def test_add_new():
    #к-во компаний
    #создать новую
    #кол-во компаний
    #проверить +1
    #проверить id последней = resp шаг 2
    #назв и описание последней компании
    body = api.get_company_list()
    len_before = len(body)
    
    nam = 'AUTO-Nemov'
    des = 'Nemov-Des'
    result = api.create_company(nam , des)
    new_id = result["id"]
    
    body = api.get_company_list()
    len_after = len(body)
 
    

    assert body[-1]["name"] == nam
    assert body[-1]["description"] == des
    assert body[-1]["id"] == new_id

def test_get_one_company():
    nam = 'Sky_INEP'
    des = 'Descr_INEP'
    result = api.create_company(nam , des)
    new_id = result["id"]
    new_company = api.get_company(new_id)

    assert new_company["id"] == new_id
    assert new_company["name"] == nam
    assert new_company["description"] == des
    
def test_edit():
        nam = 'Sky_INEP_2'
        des = 'Descr_INEP_2'
        result = api.create_company(nam , des)
        new_id = result["id"]
        new_nam = 'INEP3'
        new_des = 'DES_INEP3'

        edited = api.edit(new_id, new_nam, new_des)

        assert edited["id"] == new_id
        assert edited["name"] == new_nam
        assert edited["description"] == new_des
        assert edited["isActive"] == True

def test_del():
    nam = 'Com_to_del'
    des = 'Del_Descr_INEP_2'
    result = api.create_company(nam , des)
    new_id = result["id"]
    

    deleted = api.del_company(new_id)

    assert deleted["id"] == new_id
    assert deleted["name"] == nam
    assert deleted["description"] == des
    assert deleted["isActive"] == True
    body = api.get_company_list()
    assert body[-1]['id'] != new_id
    
def test_deactive():  
    nam = 'Deactive-Nemov'
    result = api.create_company(nam)
    new_id = result["id"]
    body = api.deactivate(new_id, False)

    assert len(body) == 7
    assert body['isActive'] == False

     
nam = 'AUTO-Nemov'
des = 'Nemov-Des'
result = api.create_company(nam , des)
print(result)
new_id = result["id"]       