 
import requests
import datetime
import pytz
import warnings
import os
import msgpack
import random
import json
import time
from ApiRes import ApiRes


class ApiSsku:

    def __init__(self, url):
        self.url = url


    
    def get_token(self, login='admin', password='adm777'): #возвращение токена с ключом
        creds = {       
            'login': login,
            'password': password,
            "hash":"49d4f2b0-4436-11ef-b7ed-0fe4a53abe63"
            }
        resp = requests.post(self.url+'/api/auth/login', json=creds, verify=False)
        bearer = (f'Bearer {resp.json()["access_token"]}')
        my_token = {
            'Authorization': bearer
        }
        return my_token
    

    def small_token(self): #возвращение только тела токена
        creds = {       
            'login': 'admin',
            'password': 'adm777'
            }
        resp = requests.post(self.url+'/api/auth/login', json=creds, verify=False)
        bearer = (f'Bearer {resp.json()["access_token"]}')
        
        return bearer


    def get_modules(self): #список модулей
        resp = requests.get(self.url+'/api/data/system/module', headers=self.get_token(), verify=False)
        return resp.json()


    def get_module_count(self): #получение количества модулей в списке
            resp = requests.get(self.url+'/api/data/system/module', headers=self.get_token(), verify=False)
            return int(len(resp.json()['data']))


    def get_module(self, i): #принимает значения для использования получения id устройства
        resp = requests.get(self.url+'/api/data/system/module', headers=self.get_token(), verify=False)
        return resp.json()['data'][i]


    def rand_id(self): #id 8-4-4-4-12
        b1 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(8)])
        b2 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(4)])
        b3 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(4)])
        b4 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(4)])
        b5 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(12)])
        full_id = (f'{b1}-{b2}-{b3}-{b4}-{b5}')
        return(full_id)


    def get_user_id(self): #получение id текущего пользователя
        resp = requests.get(self.url +'/api/data/security/user', headers = self.get_token(), verify=False)
        return resp.json()['data'][0]['id']


    def get_time(self): #формирует текущее значение времени для timestamp
        day = datetime.date.today()
        time = datetime.datetime.now(pytz.timezone('UTC')).time()
        utc_time = (f'{day}T{time}+00:00')
        return utc_time  


    def set_cams(self): #для ССКУ добавление модулей камеры в цикле с задаваемым количееством через input
        warnings.filterwarnings('ignore')
       
        i = input('количество камер: ')
        for n in range(0,int(i)):
            ip = random.choice(['172.18.18.195','192.168.202.189'])
            b = '{'+'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":"","node":"aa34df8a-41e5-445e-9b24-de9feee20414",'+f'"title":"inep_test_cam_{n+1}",'+'"zone":null,"subsystem":"video","type":"sdp850","settings":'+'{'+f'"ip":"{ip}","port":80,"maxArchiveSize":"1 GB","archiveLocation":"/archive","sourceTransport":"udp"'+'}'+'}'
            body = json.loads(b)
            resp = requests.post(self.url+'/api/data/system/module', headers=self.get_token(), json=body, verify=False)
            print(resp.json())


    def set_mock_cams(self): #для ССКУ добавление мок-камеры в цикле с задаваемым количееством через input
        warnings.filterwarnings('ignore')
       
        i = input('количество камер: ')
        for n in range(0,int(i)):
            
            b = '{'+'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":"","node":"aa34df8a-41e5-445e-9b24-de9feee20414",'+f'"title":"test_mock_{n+1}","zone":null,"subsystem":"video","type":"mockcamera","settings":'+'{'+f'"title":"test_mock_{n+1}","node":"aa34df8a-41e5-445e-9b24-de9feee20414"'+'}'+'}'
            body = json.loads(b)
            resp = requests.post(self.url+'/api/data/system/module', headers=self.get_token_g(), json=body, verify=False)
            print(resp.json()) 

        
    def notifications(self): #вывод нотификаций
            
            warnings.filterwarnings('ignore')
            os.system('cls' if os.name == 'nt' else 'clear')
            for i in range (0, self.get_module_count()):
                print(f"{i} {self.get_modules()['data'][i]['title']}"+f" тип камеры: {self.get_modules()['data'][i]['type']}")
            print('1350 потеря связи\n3350 восстановление связи\n1779 требуется калибровка\n1780 старт калибровки\n3780 конец калибровки\n1781 прерывание калибровки\n1782 калибровка успешна\n1783 калибровка неудачна\n1135 наступление дня\n3135 наступление ночи\n1321 Включение реле 1\n3321 Выключение реле 1\n1322 Включение реле 2\n3322 Выключение реле 2\n1323 Включение реле 3\n3323 Выключение реле 3\n1324 Включение реле 4\n3324 Выключение реле 4\n1502 Подготовка к выключению тепловизора\n1503 Отключение тепловизора отложено по команде оператора\n1504 Отключение тепловизора по команде оператора\n1505 Автоматическое выключение тепловизора\n3352 Объект потерян в тревожной зоне\n3351 Цель вышла из зоны тревоги\n1351 Обнаружена цель в зоне тревоги\n1792 шторка открыта\n3792 шторка открыта\n1750 Включение питания\n3750 выключение питания\n1911 критический уровень заряда\n1912 критическая температура батареи\n1913 критическая температура платы\n1914 переход в режим пониженного электропотребления\n3914 прекращение режима пониженного энергопотребления\n1910 начало заряда\n3910 конец заряда\n1130 тревога\n3130 переустановка тревоги\n1137 корпус вскрыт\n3137 корпус закрыт\n1302 разряд АКБ\n3302 восстановление АКБ\n1720 начало экспорта\n3720 экспорт завершён\n4730 ошибка экспорта\n4731 предупреждение экспорта(отмена)\n5720 отмена экспорта\n1392 начало заряда от220В\n3392 конец заряда от 220В\n1394 начало заряда от генератора \n3394 конец заряда от генератора\n1394 запуск генератора\n3395 остановка генератора\n1396 неудачный запуск генератора\n1399 уровень топлива (тревога)\n3399 уровень топива(информация)\n3911 заряд батареи в норме\n3912 температура батареи в норме\n1791 обогрев стекла включен\n3791 обогрев стекла выключен') 
            d = int(input(f'Введите номер устройства из списка: '))
            device = (self.get_module(d)['id'])
            e_code = int(input(f'Введите код нотификации для модуля <{self.get_module(d)['title']}>: '))
            time=self.get_time()    
            body = {
                "data": "", #{'gate':'fedcba098765-4321-fedc-ba09-87654321', 'card_code':'01234567'}
                "eventCode": e_code,
                "source": device,
                "timestamp": time, #"2024-06-06T08:00:00.337136+00:00"
                "user": self.get_user_id() #"51cc139c-a132-49e1-990c-786458d4415f"
                }
            i = int(input('Введите количество итераций: '))
            for _ in range (0, i):
                requests.post(self.url+'/api/data/events/history', headers=self.get_token(), json=body, verify=False)  


    def postman(self):
          warnings.filterwarnings('ignore')
          os.system('cls' if os.name == 'nt' else 'clear')
          met = input('Enter METHOD: ')
          if met.upper() == 'GET':
            uri = input('Enter uri: ')
            resp = requests.get(self.url+f'{uri}',headers=self.get_token(), verify=False)
            print(resp)
            print(msgpack.unpackb(resp))
            #print(resp.json()['data'])
          elif met.upper() == 'POST':
              uri = input('Enter uri: ')
              body_ = input('Enter Body JSON: ')
              body = json.loads(body_)  
              resp = requests.post(self.url+f'{uri}', headers=self.get_token(), json = body, verify=False)
              print(resp)
              print(resp.json()['data'])
          elif met.upper() == 'DELETE':
              uri = input('Enter uri: ')
              
              resp = requests.delete(self.url+f'{uri}', headers=self.get_token(), verify=False)
              print(resp)
              #print(resp.json())
              print(resp.json()['data'])     
                     

    def del_cams(self):
        warnings.filterwarnings('ignore')
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range (0, self.get_module_count()):
            print(f"{i} {self.get_modules()['data'][i]['title']}"+f" тип камеры: {self.get_modules()['data'][i]['type']}")
        d = int(input(f'Введите номер устройства из списка: '))
        device = (f"ids={self.get_module(d)['id']}")
        resp = requests.delete(self.url+f'/api/data/system/module',headers=self.get_token(), params=device, verify=False)
        print(resp)


    def add_node(self):
        warnings.filterwarnings('ignore')
        os.system('cls')
        nums = int(input('Введите количество серверов для добавления: '))
        for i in range(0, nums):
            body_ = '{'+'"addr": "192.168.202.9", "configPort": 7777, "enabled": true, "id":' + f' "{self.rand_id()}", "restPort": 0, "title": "test_node_{i}"'+'}'
            body = json.loads(body_)
            resp = requests.post(self.url+'/api/data/system/node',headers=self.get_token(), json=body, verify=False)
            print(resp.json())
        return(resp)


    def auth_cpu(self):
        warnings.filterwarnings('ignore')
        os.system('cls')
        cpu_title = (input('Наименование АРМа: '))
        cpu_title_body_ = '{'+f'"owner":"admin","title":"{cpu_title}","img":"","shared":false,"config":'+'{'+'"type":["auto","auto","auto","auto"],"content":[[],[],[],[]],"tabsForLayout":['+'{'+'"screenIndex":0,"type":"SOT"'+'}'+',{'+'"screenIndex":1,"type":"SOT"'+'},{'+'"screenIndex":2,"type":"ALARM_MONITOR"'+'},{'+'"screenIndex":3,"type":"INFO_MONITOR"}]'+'}'+'}'
        cpu_title_body = json.loads(cpu_title_body_) 
        layout_resp = requests.post(self.url+'/api/data/ui/layout',headers=self.get_token(), json=cpu_title_body,verify=False)
        print(f'POST layout {layout_resp.status_code}')
        cpu_id = input('CPU ID: ')
        put_arm_body_ = '{'+'"archived":false,"data":'+'{'+'"layoutImages":[{"screenIndex":0,"screenType":"SOT","iconType":null'+'},{'+'"screenIndex":1,"screenType":"SOT","iconType":null'+'},{'+'"screenIndex":2,"screenType":"ALARM_MONITOR","iconType":null'+'},{'+'"screenIndex":3,"screenType":"INFO_MONITOR","iconType":null'+'}]}'+f',"hash":"edab4970-4d9b-11ef-a454-b1120eae1a88","id":"{cpu_id}","ip":"192.168.202.61","layoutId":"40b38e92-2e9b-4c2f-b50d-fce2694e188f","name":"{cpu_title}","type":"arm-cpu","valid":true'+'}'
        put_arm_body = json.loads(put_arm_body_)
        put_arm_resp = requests.put(self.url+f'/api/data/security/arm/{cpu_id}', headers=self.get_token(), json=put_arm_body, verify=False)
        return(put_arm_resp.json())
    

    def post_incident(self):
        warnings.filterwarnings('ignore')
        os.system('cls')
        token=self.get_token()
        body_i= '{"data":{'+'"isManual":true}'+f',"event":"621f3697-56ca-4db1-adf2-0fbb212645e8","date":"{self.get_time()}","source":"ae109d47-8743-4b46-ab9e-166dc2117682"'+'}'
        body_h= '{'+f'"eventCode":4150,"source":"ae109d47-8743-4b46-ab9e-166dc2117682","timestamp":"{self.get_time()}","user":"ff7ab29a-9ad8-428c-9d68-39e8bf9cc7d1"'+'}'
        bodyi = json.loads(body_i)
        bodyh = json.loads(body_h)
        i = int(input('Количество инцидентов: )'))
        
        for _ in range(0, i):
            resp_h = requests.post(self.url+'/api/data/events/history',headers=token,json=bodyh,verify=False)
            resp_i = requests.post(self.url+'/api/data/events/incident',headers=token,json=bodyi,verify=False)
            return(resp_h, resp_i)