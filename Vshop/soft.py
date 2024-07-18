import requests
import msgpack

def get_token():
    body = {
        'login': 'admin',
        'password': 'adm777'
    }

    resp = requests.post('https://gate.synerget.ru:8179/api/auth/login', json = body, verify = False)
    bearer = (f'Bearer {resp.json()["access_token"]}')
    return bearer

def get_modules():
    token = {
        'Authorization': get_token()
    }
    resp = requests.get('https://gate.synerget.ru:8179/api/data/system/module', headers = token, verify = False)
    return resp.json()

def get_177():
    sts=''
    for i in range (0, 9):
        if get_modules()['data'][i]['title'] == 'Радиолокатор':
            sts=get_modules()['data'][i]['id']
    return sts        


   

def get_module():
    n=get_modules()
    for i in range (0, 9):
        print (n['data'][i]['title'],'-', i)
   
    module_select = input('Введите номер устройства: ')
    module_id = get_modules()['data'][int(module_select)]['id']
    print(f"ID выбранного устройства - {get_modules()['data'][int(module_select)]['title']} : {get_modules()['data'][int(module_select)]['id']}")

def add_debug():
    body ={
        'StartPoint':[2300,100],
        'EndPoint':[60,30],
        'Velocity':30
    }
    head = {
        'Authorization':get_token(),
        'content-type':'application/x-msgpack'
    }
    with open('add.msgpack','wb') as a:
        msgpack.dump(body, a)
    with open('add.msgpack', 'rb') as a:
        msgpack.load(a)    
    resp = requests.post(f'https://gate.synerget.ru:8179/api/modules/{get_177()}/AddDebugTarget', headers = head, data=a, verify=False)

body ={
        'StartPoint':[2300,100],
        'EndPoint':[60,30],
        'Velocity':30
    }
with open('add.msgpack', 'wb') as a:
    msgpack.dump(body, a)


msgpack.pack(body, b)
print(b)    