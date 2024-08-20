import requests
import datetime
import pytz
import warnings
import os
import msgpack
import random
import json
import time
from time import sleep

class ApiRes:
       
    def __init__(self, url):
        self.url = url


    def start_(self): ##
        os.system('cls' if os.name == 'nt' else 'clear')

        print('0 - выход')
        print('1 - вывод нотификаций для модулей')
        print('2 - вывод множества нотификаций для модулей')
        print('3 - добавление объектов на план-схему')
        print('4 - добавление отладочных целей на план-схему')
        print('5 - удаление панорамы')
        com = input('Введите номер скрипта: ')
        if com == '1':
            self.notifications()
        elif com == '2':
            self.notif()
        elif com == '3':
            self.add_99_targets()
        elif com == '4':
            self.add_debug()
        elif com == '5':
            self.del_panorama()
        elif com == '0':
            exit(0)
        
        self.start()    
                                 

    def get_token(self): #возвращение токена с ключом
        creds = {       
            'login': 'admin',
            'password': 'adm777'
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


    def get_time(self): #формирует текущее значение времени для timestamp
        day = datetime.date.today()
        time = datetime.datetime.now(pytz.timezone('UTC')).time()
        utc_time = (f'{day}T{time}+00:00')
        return utc_time  

   
    def get_module_count(self): #получение количества модулей в списке
            resp = requests.get(self.url+'/api/data/system/module', headers=self.get_token(), verify=False)
            return int(len(resp.json()['data']))


    def get_module(self, i): #принимает значения для использования получения id устройства
        resp = requests.get(self.url+'/api/data/system/module', headers=self.get_token(), verify=False)
        return resp.json()['data'][i]
    

    def get_user_id(self): #получение id текущего пользователя
        resp = requests.get(self.url +'/api/data/security/user', headers = self.get_token(), verify=False)
        return resp.json()['data'][0]['id']

    
    def rand_id(self): #id 8-4-4-4-12
        b1 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(8)])
        b2 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(4)])
        b3 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(4)])
        b4 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(4)])
        b5 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(12)])
        full_id = (f'{b1}-{b2}-{b3}-{b4}-{b5}')
        return(full_id)
    

    def rand_x(self): #random x для эементов план-схемы
        x1 = ''.join ([random.choice('45678' ) for _ in range(1)])
        x1_2 = ''.join ([random.choice('561234879' ) for _ in range(3)])
        x2 = ''.join ([random.choice('192837465' ) for _ in range(9)])
    
        full_x = (f'466{x1}{x1_2}.{x2}')
        return(float(full_x))
   

    def rand_y(self): #random y для эементов план-схемы
        y1 = random.choice([16,17,18,19,20])
        y1_2 = ''.join ([random.choice('561234879' ) for _ in range(3)])
        y2 = ''.join ([random.choice('192837465' ) for _ in range(9)])
    
        full_y = (f'56{y1}{y1_2}.{y2}')
        return(float(full_y))
    
    
    def rand_icon(self): #random icon для эементов план-схемы
        icon = random.choice(['icon_plane','icon_tank','icon_bomb','icon_helic','icon_camp','icon_ship'])
        return(icon)
    

    def notifications_(self): ##
            warnings.filterwarnings('ignore')
            os.system('cls' if os.name == 'nt' else 'clear')
            mc = int(self.get_module_count())
            print (f'var mc == {mc}')
            for i in range (0, mc):
                print(f"{i} {self.get_modules()['data'][i]['title']}")
            d = int(input(f'Введите номер устройства из списка: '))
            device = (self.get_module(d)['id'])
            os.system('cls' if os.name == 'nt' else 'clear')
            print('1350 потеря связи\n3350 восстановление связи\n1779 требуется калибровка\n1780 старт калибровки\n3780 конец калибровки\n1781 прерывание калибровки\n1782 калибровка успешна\n1783 калибровка неудачна\n1135 наступление дня\n3135 наступление ночи\n1321 Включение реле 1\n3321 Выключение реле 1\n1322 Включение реле 2\n3322 Выключение реле 2\n1323 Включение реле 3\n3323 Выключение реле 3\n1324 Включение реле 4\n3324 Выключение реле 4\n1502 Подготовка к выключению тепловизора\n1503 Отключение тепловизора отложено по команде оператора\n1504 Отключение тепловизора по команде оператора\n1505 Автоматическое выключение тепловизора\n3352 Объект потерян в тревожной зоне\n3351 Цель вышла из зоны тревоги\n1351 Обнаружена цель в зоне тревоги\n1792 шторка открыта\n3792 шторка открыта\n1750 Включение питания\n3750 выключение питания\n1911 критический уровень заряда\n1912 критическая температура батареи\n1913 критическая температура платы\n1914 переход в режим пониженного электропотребления\n3914 прекращение режима пониженного энергопотребления\n1910 начало заряда\n3910 конец заряда\n1130 тревога\n3130 переустановка тревоги\n1137 корпус вскрыт\n3137 корпус закрыт\n1302 разряд АКБ\n3302 восстановление АКБ\n1720 начало экспорта\n3720 экспорт завершён\n4730 ошибка экспорта\n4731 предупреждение экспорта(отмена)\n5720 отмена экспорта\n1392 начало заряда от220В\n3392 конец заряда от 220В\n1394 начало заряда от генератора \n3394 конец заряда от генератора\n1394 запуск генератора\n3395 остановка генератора\n1396 неудачный запуск генератора\n1399 уровень топлива (тревога)\n3399 уровень топива(информация)\n3911 заряд батареи в норме\n3912 температура батареи в норме\n1791 обогрев стекла включен\n3791 обогрев стекла выключен') 
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


    def notifications(self): #вывод нотификаций
            warnings.filterwarnings('ignore')
            os.system('cls' if os.name == 'nt' else 'clear')
            for i in range (0, self.get_module_count()):
                print(f"{i} {self.get_modules()['data'][i]['title']}")
            d = int(input(f'Введите номер устройства из списка: '))
            device = (self.get_module(d)['id'])
            os.system('cls' if os.name == 'nt' else 'clear')
            if self.get_module(d)['type'] == 'astcclient':
                print(f'Для модуля <{self.get_module(d)['title']}> нет нотификаций')
                
            elif self.get_module(d)['type'] == 'objectdetector':
                print(f'Для модуля <{self.get_module(d)['title']}> нет нотификаций')
                    
            elif self.get_module(d)['type'] == 'stl724':
                print(f'Для модуля <{self.get_module(d)['title']}> доступны следующие коды нотификации: \n')
                print('1350 потеря связи\n3350 восстановление связи\n1392 начало заряда от220В\n3392 конец заряда от 220ВВ\n1394 начало заряда от генератора \n3394 конец заряда от генератора\n1394 запуск генератора\n3395 остановка генератора\n1396 неудачный запуск генератора\n1399 уровень топлива (тревога)\n3399 уровень топива(информация)\n1911 критический заряд батареи\n3911 заряд батареи в норме\n1912 критическая температура батареи\n3912 температура батареи в норме')
            elif self.get_module(d)['type'] == 'stl725':
                print(f'Для модуля <{self.get_module(d)['title']}> доступны следующие коды нотификации: \n')
                print('1350 потеря связи\n3350 восстановление связи\n1911 критический заряд батареи\n1912 критическая температура батареи\n1913 критическая температура платы\n1914 переход в режим пониженного электропотребления\n3914 прекращение режима пониженного электропотребления\n1910 начало заряда\n3910 конец заряда')
            elif self.get_module(d)['type'] == 'sts507':
                print(f'Для модуля <{self.get_module(d)['title']}> доступны следующие коды нотификации: \n')
                print('1350 потеря связи\n3350 восстановление связи')
            elif self.get_module(d)['type'] == 'termalcamera':
                print(f'Для модуля <{self.get_module(d)['title']}> доступны следующие коды нотификации: \n')  
                print('1350 потеря связи\n3350 восстановление связи\n1792 шторка открыта\n3792 шторка закрыта\n1750 выключение питания\n3750 выключение питания\n')
            elif self.get_module(d)['type'] == 'sdp881':
                print(f'Для модуля <{self.get_module(d)['title']}> доступны следующие коды нотификации: \n')
                print('1350 потеря связи\n3350 восстановление связи\n1779 требуется калибровка\n1780 старт калибровки\n3780 конец калибровки\n1781 прерывание калибровки\n1782 калибровка успешна\n1783 калибровка неудачна\n1135 наступление дня\n3135 наступление ночи\n1321 Включение реле 1\n3321 Выключение реле 1\n1322 Включение реле 2\n3322 Выключение реле 2\n1323 Включение реле 3\n3323 Выключение реле 3\n1324 Включение реле 4\n3324 Выключение реле 4\n1502 Подготовка к выключению тепловизора\n1503 Отключение тепловизора отложено по команде оператора\n1504 Отключение тепловизора по команде оператора\n1505 Автоматическое выключение тепловизора')
            elif self.get_module(d)['type'] == 'sts177':
                print(f'Для модуля <{self.get_module(d)['title']}> доступны следующие коды нотификации: \n')
                print('1350 потеря связи\n3350 восстановление связи\n3352 Объект потерян в тревожной зоне\n3351 Цель вышла из зоны тревоги\n1351 Обнаружена цель в зоне тревоги')
            elif self.get_module(d)['type'] == 'sdp8083':
                print(f'Для модуля <{self.get_module(d)['title']}> доступны следующие коды нотификации: \n')
                print('1350 потеря связи\n3350 восстановление связи\n1750 включение питания\n3750 выключение питания\n1791 обогрев стекла включен\n3791 обогрев стекла выключен')
            elif self.get_module(d)['type'] == 'brdmk':
                print(f'Для модуля <{self.get_module(d)['title']}> доступны следующие коды нотификации: \n')
                print('1350 потеря связи\n3350 восстановление связи\n1130 тревога\n3130 переустановка связи\n1137 корпус вскрыт\n3137 корпус закрыт\n1302 разряд АКБ\n3302 восстановление АКБ')
            elif self.get_module(d)['type'] == 'onvifcamera':
                print(f'Для модуля <{self.get_module(d)['title']}> доступны следующие коды нотификации: \n')
                print('1350 потеря связи\n3350 восстановление связи')
                

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
                          
            
    def get_zone(self): #получение id зоны
        resp = requests.get(self.url+'/api/data/system/zone', headers = self.get_token(), verify=False)
        return resp.json()['data'][0]['id']
    

    def get_177(self): #получение id радиолокатора
       
        for i in range (0, int(self.get_module_count())):
            sts_ch = (self.get_modules()['data'][i]['title'])
            if sts_ch == 'Радиолокатор':
                d = i
        
        sts177 = (self.get_module(d)['id'])
        return sts177
    

    def get_881(self): #получение id поворотного
        os.system('cls' if os.name == 'nt' else 'clear')
        warnings.filterwarnings('ignore')
        for i in range (0, int(self.get_module_count())):
            sts_ch = (self.get_modules()['data'][i]['title'])
            if sts_ch == 'Поворотное устройство':
                d = i
        
        sts881 = (self.get_module(d)['id'])
        return sts881


    def get_8083(self): #получение id камеры8083
        os.system('cls' if os.name == 'nt' else 'clear')
        warnings.filterwarnings('ignore')
        for i in range (0, 10):
            sts_ch = (self.get_modules()['data'][i]['type'])
            if sts_ch == 'sdp8083':
                d = i
        sdp8083 = (self.get_module(d)['id'])     
        return sdp8083
    

    def get_8815(self): #получение id тепловизора8815
        os.system('cls' if os.name == 'nt' else 'clear')
        warnings.filterwarnings('ignore')
        for i in range (0, 10):
            sts_ch = (self.get_modules()['data'][i]['type'])
            if sts_ch == 'termalcamera':
                d = i
        sdp8815 = (self.get_module(d)['id'])  
        return sdp8815


    def add_debug(self): #добавление отладочных целей 
        os.system('cls' if os.name == 'nt' else 'clear')
        i = input('Количество отладочных целей: ')
        for _ in range (0, int(i)):
            warnings.filterwarnings('ignore')
            
            head = {
                'Authorization': self.small_token(),
                'Content-type': 'application/x-msgpack'
                }
            
            sp1 = random.randint(800, 2300)
            sp2 = random.randint(525, 1500)
            ep1 = random.randint(20, 500)
            ep2 = random.randint(100,800)
            v = random.randint(40,120)

            body = {"debugTarget":{"startPoint":[sp1, sp2],"endPoint":[ep1, ep2],"velocity":v}}
            msp = msgpack.packb(body)
            resp = requests.post(self.url +'/api/modules/'+self.get_177()+'/AddDebugTarget', headers=head, data=msp, verify=False)
            
        print(resp)
        yn = input('Удалить отладочные цели?(y/n): ')
        if yn =='y':
            self.del_debug()
        #else:
            #return('no del')
            

    def notif(self): #генерация множества нотификаций
            time_start = datetime.datetime.now()
            warnings.filterwarnings('ignore')
            os.system('cls' if os.name == 'nt' else 'clear')
            itr = int(input('Введите количество итераций: '))
            for _ in range (0, itr):
                rand_device = random.randint(0,self.get_module_count()-1)
                                
                on_off = ['1350', '3350']
                                              
                body = {
                    "data": "", 
                    "eventCode": int(random.choice(on_off)),
                    "source": self.get_module(rand_device)['id'],
                    "timestamp": self.get_time(), #"2024-06-06T08:00:00.337136+00:00"
                    "user": self.get_user_id() #"51cc139c-a132-49e1-990c-786458d4415f"
                    }
            
                ran_resp = requests.post(self.url+'/api/data/events/history', headers=self.get_token(), json=body, verify=False)
                print(ran_resp)
                                
            time_fin=datetime.datetime.now()
            print(time_fin-time_start)
                

    def del_debug(self): #удаление отладочных целей
        warnings.filterwarnings('ignore')
        os.system('cls' if os.name == 'nt' else 'clear')
        head = {
            'Authorization': self.small_token(),
            'Content-type': 'application/x-msgpack'
            }                
        nul=None
        msp_null = msgpack.packb(nul) 
        requests.post(self.url +'/api/modules/'+ self.get_177() +'/ResetDebugTargets', headers = head, data=msp_null, verify = False)


    def rand_targets(self, i): #генерация json с random id, icon, title, x, y
        rnd_icon = self.rand_icon()
        if rnd_icon == 'icon_plane':
            tit = '<самолёт>' 
        elif rnd_icon == 'icon_tank':
            tit = '<танк>'
        elif rnd_icon == 'icon_bomb':
            tit = '<бомба>'
        elif rnd_icon == 'icon_helic':
            tit = '<вертолёт>'
        elif rnd_icon == 'icon_camp':
            tit = '<штаб>'
        elif rnd_icon == 'icon_ship':
            tit = '<корабль>'
            
        block_b = '{"fontSize":14,'+f'"id":"{self.rand_id()}"'+',"locked":false,"polygon":[],'+f'"schemaName":"{rnd_icon}",'+'"sourceID":"","sourceType":"static_icon",'+f'"title":"{i+1} тестовый объект {tit}",'+'"type":"static_icon",'+f'"x":{self.rand_x()},"y":{self.rand_y()}'+'},'
        
        return (block_b)

        
    def add_99_targets(self): #добавление элементов на план-схему
            warnings.filterwarnings('ignore')
            os.system('cls' if os.name == 'nt' else 'clear')
            self.del_targets()

            block_open = '{"title":"Murom","settings":{"backgroundImage":"","items":[{"fontSize":0,"id":"946aa060-24ae-11ef-b321-c905af5a3e46","locked":false,"polygon":[],"sourceID":"","sourceType":"murom","title":"Комплекс Муром-П","type":"icon","x":41.920834,"y":44.983891},'
            
            hm = input('Сколько тестовых элементов добавить на план-схему?: ')  

            many_blocks = ''
            
            for i in range(int(hm)-1):
                    many_blocks = many_blocks + self.rand_targets(i)
                                               
            block_close = '{"fontSize":14,"id":"628745aa-7aae-435b-bed9-130c4fb3b65d","locked":false,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon",'+f'"title":"{i+2} тестовый объект <самолёт>",'+'"type":"static_icon","x":4664668.550394735,"y":5621110.639272644}],"sxfMaps":{"apiUrl":"http://10.201.0.1:5634","layerIds":[]}}}'
              
            body = json.loads(block_open + many_blocks + block_close) 
            resp = requests.put(self.url+'/api/data/system/zone/'+self.get_zone(), headers=self.get_token(), json=body, verify=False)
            print(resp)
            yn = input('Удалить объекты с план-схемы?(y/n): ')
            if yn =='y':
                self.del_targets()
            else:
                return None          


    def del_targets(self): #удаление всех элементов с план-схемы
        
        body ={"title":"Murom","settings":{"backgroundImage":"Custom:http://10.201.0.1:13370","items":[{"fontSize":0,"id":"2cb06ef0-dcf2-11ed-b84f-07d68e1078e7","locked":False,"polygon":[],"sourceID":"","sourceType":"murom","title":"Комплекс Муром-П","type":"icon","x":41.921112,"y":44.983612}],"sxfMaps":{"apiUrl":"http://10.201.0.1:5634","layerIds":[]}}}
        
        requests.put(self.url+'/api/data/system/zone/'+self.get_zone(), headers=self.get_token(), json=body, verify=False)


    def del_panorama(self): #удаление панорамы
        body = {"image": ""}
        requests.post(self.url+'/api/data/ui/panorama', headers=self.get_token(), json=body, verify=False)


    def set_cams(self): #для Гелиос добавление модулей камеры в цикле с задаваемым количееством через input
        warnings.filterwarnings('ignore')
        head = {'Authorization': self.small_token()
            }
        i = input('количество камер: ')
        for n in range(0,int(i)):
            ip = random.choice(['172.18.18.141'])
            b = '{'+'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":"","node":"0c933048-e954-48eb-b1cf-563812070c5d",'+f'"title":"test_cam_{n+1}",'+'"zone":null,"subsystem":"video","type":"onvifcamera","settings":'+'{'+f'"ip":"{ip}","port":80,"onvif":'+'{'+'"login":"admin","password":"admin"'+'}'+',"webrtc":'+'{'+'"startVideoHeight":300'+'}'+',"rtsp":{"sourceTransport":["tcp","udp"]},"archive":{"maxArchiveSize":"1 GB","archiveLocation":"../archive","mode":"write"}}}'
            body = json.loads(b)
            resp = requests.post(self.url+'/api/data/system/module', headers=head, json=body, verify=False)
            print(resp.json())        
       

    def change_ip(self): #смена ip камеры и тепловизора поочерёдно
        
        ip_141 = '172.18.18.141'
        ip_189 = '172.18.18.189'
        pro = ''
        n = input('Количество итераций: ')
        for i in range (0, int(n)):
            if (i%2):
                b_1 = '{'+'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000",'+f'"id":"{self.get_8083()}",' + '"node":"2d67fd8d-8945-4814-95e1-9903746ac527","title":"Камера дальнего обзора","zone":null,"subsystem":"video","type":"sdp8083","settings":'+'{'+f'"ip":"{ip_141}","port":80,"onvif":'+'{'+'"login":"admin","password":"admin"'+'}'+'}'+'}'
                b_2 = '{'+'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000",'+f'"id":"{self.get_8815()}",' + '"node":"2d67fd8d-8945-4814-95e1-9903746ac527","title":"Камера тепловизионная","zone":null,"subsystem":"video","type":"termalcamera","settings":'+'{'+f'"ip":"{ip_189}","port":80,"deviceType":"svk8815m"'+'}'+'}'   
                body_1 = json.loads(b_1)
                body_2 = json.loads(b_2)
                requests.put(self.url+'/api/data/system/module/'+self.get_8083(), headers=self.get_token(), json=body_1, verify=False)
                requests.put(self.url+'/api/data/system/module/'+self.get_8815(), headers=self.get_token(), json=body_2, verify=False)
                pro = pro + '|'
                print(pro)
                time.sleep(30) 
            else:
                b_1 = '{'+'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000",'+f'"id":"{self.get_8083()}",' + '"node":"2d67fd8d-8945-4814-95e1-9903746ac527","title":"Камера дальнего обзора","zone":null,"subsystem":"video","type":"sdp8083","settings":'+'{'+f'"ip":"{ip_189}","port":80,"onvif":'+'{'+'"login":"admin","password":"admin"'+'}'+'}'+'}'
                b_2 = '{'+'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000",'+f'"id":"{self.get_8815()}",' + '"node":"2d67fd8d-8945-4814-95e1-9903746ac527","title":"Камера тепловизионная","zone":null,"subsystem":"video","type":"termalcamera","settings":'+'{'+f'"ip":"{ip_141}","port":80,"deviceType":"svk8815m"'+'}'+'}'   
                body_1 = json.loads(b_1)
                body_2 = json.loads(b_2)
                requests.put(self.url+'/api/data/system/module/'+self.get_8083(), headers=self.get_token(), json=body_1, verify=False)
                requests.put(self.url+'/api/data/system/module/'+self.get_8815(), headers=self.get_token(), json=body_2, verify=False)
                pro = pro + '|'
                print(pro)
                time.sleep(30) 
                       
    
    def norm_ip(self): #восстановление по дефлоту камер
        ip_141 = '172.18.18.141'
        ip_189 = '172.18.18.189'
        b_1 = '{'+'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000",'+f'"id":"53369faa-37f1-41fd-a54b-ed6d10af663d",' + '"node":"2d67fd8d-8945-4814-95e1-9903746ac527","title":"Камера дальнего обзора","zone":null,"subsystem":"video","type":"sdp8083","settings":'+'{'+f'"ip":"{ip_141}","port":80,"onvif":'+'{'+'"login":"admin","password":"admin"'+'}'+'}'+'}'
        b_2 = '{'+'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000",'+f'"id":"62e5c253-1b3e-4bf4-9111-1daac5e5d53f",' + '"node":"2d67fd8d-8945-4814-95e1-9903746ac527","title":"Камера тепловизионная","zone":null,"subsystem":"video","type":"termalcamera","settings":'+'{'+f'"ip":"{ip_189}","port":80,"deviceType":"svk8815m"'+'}'+'}'   
        body_1 = json.loads(b_1)
        body_2 = json.loads(b_2)
        requests.put(self.url+'/api/data/system/module/53369faa-37f1-41fd-a54b-ed6d10af663d', headers=self.get_token(), json=body_1, verify=False)
        requests.put(self.url+'/api/data/system/module/62e5c253-1b3e-4bf4-9111-1daac5e5d53f', headers=self.get_token(), json=body_2, verify=False)


    def add_users(self): #добавление множества пользователей
        warnings.filterwarnings('ignore')
        i = int(input('Введите количество пользователей: '))
        for num in range(0, i):

            name = f'test_user_{num+1}'
            login = f'test_user_{num+1}'
            password = f'test_user_{num+1}'

            b = '{'+f'"name":"{name}","login":"{login}","password":"{password}","confirmPassword":"{password}","role":"Администратор","surname":"","middleName":""'+'}'
            body =json.loads(b)
            resp = requests.post(self.url+'/api/data/security/user', headers=self.get_token(), json=body, verify=False)
        


    def add_user(self): #добавление пользователя с input
        warnings.filterwarnings('ignore')
        name = input('Введите имя: ')
        login = input('Введите логин: ')
        password = input('Введите пароль: ')

        b = '{'+f'"name":"{name}","login":"{login}","password":"{password}","confirmPassword":"{password}","role":"Администратор","surname":"","middleName":""'+'}'
        body = json.loads(b)
        resp = requests.post(self.url+'/api/data/security/user', headers=self.get_token(), json=body, verify=False) 
        return(resp)
        time.sleep(3)


    def add_layout(self):
        warnings.filterwarnings('ignore')
        i = int(input('Введите количество раскладок: '))
        for n in range(0, i):
            b = '{'+f'"owner":"admin","config":'+'{'+'"content":['+'{'+f'"id":"{self.rand_id}","type":"video"'+'}'+'],"type":"1","isAuto":false,"armType":""'+'}'+',"img":"","shared":true,"title":'+f'"test_layout_{n+1}"'+'}'
            body = json.loads(b)
            requests.post(self.url+'/api/data/ui/layout', headers=self.get_token(), json=body, verify=False)

    def del_layouts(self):
        warnings.filterwarnings('ignore')
        body ={}
        lay = requests.post(self.url+'/api/data/ui/layout/shared', headers=self.get_token(),json=body, verify=False)
        len_lay =lay.json()['data']
        for i in range(0, int(len(len_lay))):
            del_id = (lay.json()['data'][i]['id'])
            requests.delete(self.url+f'/api/data/ui/layout/{del_id}',headers=self.get_token(),verify=False)







