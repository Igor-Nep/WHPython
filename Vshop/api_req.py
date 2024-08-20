from ApiRes import ApiRes
from ApiSsku import ApiSsku
import requests
import msgpack
import json
import os
import time
import warnings

base_url = 'https://gate.synerget.ru:8179'
api = ApiRes(base_url)
ssku = ApiSsku(base_url)

def start():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('1 - Муром')
    print('2 - Гелиос')
    print('3 - ССКУ')
    spo = input('Введите номер проекта: ')
    if spo =='1':
        
        print('0 - выход')
        print('1 - вывод нотификаций для модулей')
        print('2 - вывод множества нотификаций для модулей')
        print('3 - добавление объектов на план-схему')
        print('4 - добавление отладочных целей на план-схему')
        print('5 - удаление панорамы')
        print('6 - добавление пользователя')
        print('7 - добавление множества пользователей')
        print('8 - смена камер в ячейках попеременно')
        com = input('Введите номер скрипта: ')
        if com == '1':
            api.notifications()
        elif com == '2':
            api.notif()
        elif com == '3':
            api.add_99_targets()
        elif com == '4':
            api.add_debug()
        elif com == '5':
            api.del_panorama()
        elif com == '6':
            api.add_user()
        elif com == '7':
            api.add_users()
        elif com == '8':
            api.change_ip()    
        elif com == '0':
            exit(0)
        time.sleep(4)    
        start()

    elif spo == '2':
        print('0 -выход')
        print('1 - добавление пользователя')
        print('2 - добавление множества пользователей')
        print('3 - добавление камер(модулей)')
        print('4 - вывод нотификаций для модуля')
        print('5 - вывод множества нотификаций для модулей')
        com_g = input('введите номер скрипта: ')
        if com_g == '0':
            exit(0)
        elif com_g == '1':
            api.add_user()
        elif com_g == '2':
            api.add_users()    
        elif com_g == '3':
            api.set_cams()
        elif com_g == '4':
            api.notifications()
        elif com_g =='5':
            api.notif()                
        start()

    elif spo == '3':
        print('1 - добавление камер')
        print('2 - добавление моковой камеры')
        print('3 - удаление модуля')
        print('4 - вывод нотификаций')
        print('5 - постман')
        print('6 - ручной инцидент с камеры')
        com_ssku = input('Введите номер скрипта: ')
        if  com_ssku == '1':
            ssku.set_cams()
        elif com_ssku == '2':
            ssku.set_mock_cams()
        elif com_ssku == '3':
            ssku.del_cams()    
        elif com_ssku == '4':
            ssku.notifications()
        elif com_ssku == '5':
            ssku.postman()
        elif com_ssku == '6':
            ssku.post_incident()
        #start()  
        

#start() 
#api.del_layouts()
#api.add_layout()



def get_presets():
    warnings.filterwarnings('ignore')
    head = {
            'Authorization': api.small_token(),
            'Content-type': 'application/x-msgpack'
            }
    msp_null = msgpack.packb(None) 
    resp = requests.post('https://gate.synerget.ru:8179/api/modules/'+ api.get_881() +'/PTZGetPresets', headers = head, data=msp_null, verify = False)
    
    return (msgpack.unpackb(resp.content))


def get_servers():
    
    resp = requests.get(base_url+'/api/data/system/node',headers=ssku.get_token(), verify=False)
    
    return (resp.json())

def get_node_list():
    body_ = {"limit": 1, "offset": 1, "sort": "test_node_3", "sortAsc":True, "title": "test_node_3"}
    resp = requests.post(base_url+'/api/data/system/node/list',headers=ssku.get_token(), json=body_, verify=False)
    return(resp.json())


def mode_read():
    warnings.filterwarnings('ignore')
    body_ = '{'+'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":"7c51643b-9d17-4af5-bb18-68addd812c4c","node":"0c933048-e954-48eb-b1cf-563812070c5d","title":"test_cam_1_read","zone":null,"subsystem":"video","type":"onvifcamera","settings":{"ip":"172.18.18.141","port":80,"onvif":{"login":"admin","password":"admin"},"webrtc":{"startVideoHeight":300},"rtsp":{"sourceTransport":["tcp","udp"]},"archive":{"maxArchiveSize":"1 GB","archiveLocation":"../archive","mode":"read"'+'}'+'}'+'}'
    body = json.loads(body_)
    resp = requests.put(base_url+'/api/data/system/module/7c51643b-9d17-4af5-bb18-68addd812c4c',headers=api.get_token(), json = body, verify=False)
    return(resp)


def add_user_murom(): #добавление пользователя с input
    warnings.filterwarnings('ignore')
    name = input('Введите имя: ')
    login = input('Введите логин: ')
    password = input('Введите пароль: ')

    b = '{'+f'"name":"{name}","login":"{login}","password":"{password}","accessCard":"","role":"admin", "active":true, "surname":"","middleName":"", "data":'+'{'+'}'+'}'
    body = json.loads(b)
    resp = requests.post(base_url+'/api/data/security/user', headers=api.get_token(), json=body, verify=False) 
    return(resp)
    

print(ssku.post_incident())
#print(add_user_murom())
#print(mode_read())
#print(get_node_list())
#print(ssku.add_node())
#print(ssku.auth_cpu())
