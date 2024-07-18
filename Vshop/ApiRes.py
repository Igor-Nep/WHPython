import requests
import datetime
import pytz
import warnings
import os
import msgpack
import random
import json

class ApiRes:
       
    def __init__(self, url):
        self.url = url


    def start(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print('0 - выход')
        print('1 - вывод нотификаций для модулей')
        print('2 - вывод множества нотификаций для модулей')
        print('3 - добавление 99 целей на план-схему')
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
                                 

    def get_token(self):
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
    

    def small_token(self):
        creds = {       
            'login': 'admin',
            'password': 'adm777'
            }
        resp = requests.post(self.url+'/api/auth/login', json=creds, verify=False)
        bearer = (f'Bearer {resp.json()["access_token"]}')
        
        return bearer


    def get_modules(self):
        resp = requests.get(self.url+'/api/data/system/module', headers=self.get_token(), verify=False)
        return resp.json()


    def get_time(self):
        day = datetime.date.today()
        time = datetime.datetime.now(pytz.timezone('UTC')).time()
        utc_time = (f'{day}T{time}+00:00')
        return utc_time  


    def get_module(self, i):
        resp = requests.get(self.url+'/api/data/system/module', headers=self.get_token(), verify=False)
        return resp.json()['data'][i]
    

    def get_user_id(self):
        resp = requests.get(self.url +'/api/data/security/user', headers = self.get_token(), verify=False)
        return resp.json()['data'][0]['id']

    
    def rand_id(self):
        b1 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(8)])
        b2 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(4)])
        b3 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(4)])
        b4 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(4)])
        b5 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(12)])
        full_id = (f'{b1}-{b2}-{b3}-{b4}-{b5}')
        return(full_id)
    

    def rand_x(self):
        x1 = ''.join ([random.choice('45678' ) for _ in range(1)])
        x1_2 = ''.join ([random.choice('561234879' ) for _ in range(3)])
        x2 = ''.join ([random.choice('192837465' ) for _ in range(9)])
    
        full_x = (f'466{x1}{x1_2}.{x2}')
        return(float(full_x))
    

    def rand_y(self):
        y1 = random.choice([16,17,18,19,20])
        y1_2 = ''.join ([random.choice('561234879' ) for _ in range(3)])
        y2 = ''.join ([random.choice('192837465' ) for _ in range(9)])
    
        full_y = (f'56{y1}{y1_2}.{y2}')
        return(float(full_y))
    
    
    def rand_icon(self):
        icon = random.choice(['icon_plane','icon_tank','icon_bomb','icon_helic','icon_camp','icon_ship'])
        return(icon)
    

    def notifications_(self):
            warnings.filterwarnings('ignore')
            os.system('cls' if os.name == 'nt' else 'clear')
            for i in range (0, 10):
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


    def notifications(self):
            warnings.filterwarnings('ignore')
            os.system('cls' if os.name == 'nt' else 'clear')
            for i in range (0, 10):
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
                          
            
    def get_zone(self):
        resp = requests.get(self.url+'/api/data/system/zone', headers = self.get_token(), verify=False)
        return resp.json()['data'][0]['id']
    

    def get_177(self):
       
        for i in range (0, 9):
            sts_ch = (self.get_modules()['data'][i]['title'])
            if sts_ch == 'Радиолокатор':
                d = i
        
        sts177 = (self.get_module(d)['id'])
        return sts177


    def add_debug(self):
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

            body = {"debugTarget":{"startPoint":[sp1,sp2],"endPoint":[ep1, ep2],"velocity":v}}
            msp = msgpack.packb(body)
            resp = requests.post(self.url +'/api/modules/'+self.get_177()+'/AddDebugTarget', headers=head, data=msp, verify=False)
            
        print(resp)
        yn = input('Удалить отладочные цели?(y/n): ')
        if yn =='y':
            self.del_debug()
        else:
            return('no del')
            

    def notif(self):
            time_start = datetime.datetime.now()
            warnings.filterwarnings('ignore')
            os.system('cls' if os.name == 'nt' else 'clear')
            itr = int(input('Введите количество итераций: '))
            for _ in range (0, itr):
                rand_device = random.randint(0,9)
                                
                on_off = ['1350', '3350']
                                              
                body = {
                    "data": "", 
                    "eventCode": int(random.choice(on_off)),
                    "source": self.get_module(int(rand_device))['id'],
                    "timestamp": self.get_time(), #"2024-06-06T08:00:00.337136+00:00"
                    "user": self.get_user_id() #"51cc139c-a132-49e1-990c-786458d4415f"
                    }
            
                ran_resp = requests.post(self.url+'/api/data/events/history', headers=self.get_token(), json=body, verify=False)
                print(ran_resp)
                                
            time_fin=datetime.datetime.now()
            print(time_fin-time_start)
                

    def del_debug(self):
        warnings.filterwarnings('ignore')
        os.system('cls' if os.name == 'nt' else 'clear')
        head = {
            'Authorization': self.small_token(),
            'Content-type': 'application/x-msgpack'
            }                
        nul=None
        msp_null = msgpack.packb(nul) 
        requests.post(self.url +'/api/modules/'+ self.get_177() +'/ResetDebugTargets', headers = head, data=msp_null, verify = False)


    def add_99_targets_(self):
        warnings.filterwarnings('ignore')
        os.system('cls' if os.name == 'nt' else 'clear')
        self.del_targets()
              
        body = {"title":"Murom","settings":{"backgroundImage":"","items":[{"fontSize":0,"id":"946aa060-24ae-11ef-b321-c905af5a3e46","locked":False,"polygon":[],"sourceID":"","sourceType":"murom","title":"Комплекс Муром-П","type":"icon","x":41.920834,"y":44.983891},{"fontSize":14,"id":"628745aa-7aae-435b-bed9-130c4fb3b65d","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4664668.550394735,"y":5621110.639272644},{"fontSize":14,"id":"65467d95-88e5-4904-a20e-f1c25d672629","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4664963.981168811,"y":5620815.208498568},{"fontSize":14,"id":"9b6cd940-035b-4ef9-a9b1-2f8761ae8f1b","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4665213.961054568,"y":5620587.954056971},{"fontSize":14,"id":"970707db-ae9d-4879-b7ea-eca95b85ac0e","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4665498.029106564,"y":5620281.160560815},{"fontSize":14,"id":"0d22440b-9164-4f84-97fe-471c00d42bbb","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4665782.0971585605,"y":5619997.092508819},{"fontSize":14,"id":"2855924f-b618-4128-8147-43542ab48d0e","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4666100.253376797,"y":5619656.210846423},{"fontSize":14,"id":"5a6c28a4-3d71-405d-bd30-30e71e8cd78a","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4666429.772317112,"y":5619349.417350267},{"fontSize":14,"id":"d5fab381-de36-4634-b5da-280c58a1de55","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4666764.18189275,"y":5619018.258702543},{"fontSize":14,"id":"da007acf-6339-4559-a8a5-2e0d39dc1512","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4667088.810197744,"y":5618735.830357955},{"fontSize":14,"id":"697c8074-9dbe-490c-a2ac-970f33d4c434","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4667452.417304299,"y":5618417.674139719},{"fontSize":14,"id":"c1542378-02df-449c-8a7f-97c5a430734c","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4667804.661688775,"y":5618099.517921483},{"fontSize":14,"id":"bb3ebfb9-e3ae-4f9e-9bb9-ddae7220f8a0","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4668156.90607325,"y":5617758.636259087},{"fontSize":14,"id":"98b8043c-1ff9-4375-aee6-7a923a644561","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4668463.699569406,"y":5617395.029152532},{"fontSize":14,"id":"fb7f43a6-2e80-4fe5-a53e-eb44b3f3d0b0","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4668793.218509722,"y":5617042.784768057},{"fontSize":14,"id":"9cdffa37-7a09-4662-a999-52351adaab8f","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4669145.462894198,"y":5616701.903105661},{"fontSize":14,"id":"0b9e2197-a643-4ee4-b54a-e3272a7de1c5","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4665634.381771523,"y":5621349.256436321},{"fontSize":14,"id":"ba87006d-849e-423d-9a12-02dc9521d81d","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4666009.351600158,"y":5620997.012051846},{"fontSize":14,"id":"9d5cdc4e-1d8f-4c8d-a64d-f0e08704b061","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4666429.772317112,"y":5620656.13038945},{"fontSize":14,"id":"fe2f6871-975c-4be5-93ad-a2fb72ffdedc","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4666850.193034067,"y":5620281.160560815},{"fontSize":14,"id":"cbfc6c32-8f97-4331-8c47-bf4c1de70f7d","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4667202.437418542,"y":5619997.092508819},{"fontSize":14,"id":"2b4f03eb-a552-4bb7-97fb-141231682aa2","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4667540.039569157,"y":5619678.90739649},{"fontSize":14,"id":"68dd4ea1-ee36-4140-947b-c6b28666b6e4","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4667906.926187493,"y":5619349.417350267},{"fontSize":14,"id":"6228e445-b4b2-443d-a239-38924466d537","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4668247.807849889,"y":5619031.261132031},{"fontSize":14,"id":"46d3a5d5-0138-4432-bc80-8576d604fb78","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4668588.6895122845,"y":5618701.742191715},{"fontSize":14,"id":"be6da098-49f0-4cbd-936d-277dfd0c6dc4","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4668929.57117468,"y":5618406.311417639},{"fontSize":14,"id":"0ea8d5af-d416-40be-a03c-050670b8d09b","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4664384.482342739,"y":5620190.258784176},{"fontSize":14,"id":"f8ab1e05-7882-49ff-ad14-84e9ba85b05a","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4664770.814893453,"y":5619872.1025659405},{"fontSize":14,"id":"626da78a-1128-4589-8263-5c7606910ca3","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4665088.97111169,"y":5619599.397236024},{"fontSize":14,"id":"ae8249f2-5e51-4d1f-85dc-0e3c4e1c8c27","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4665441.215496165,"y":5619269.878295708},{"fontSize":14,"id":"cdefc7d8-38b9-4c02-b8a0-2aa19b7c6431","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4665748.008992321,"y":5618985.810243712},{"fontSize":14,"id":"cae388e4-2214-4805-b64b-9fb8f1a6a3ae","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4666056.442244368,"y":5618666.072106252},{"fontSize":14,"id":"4508e3b5-0ea9-4258-9dfb-79cbcba48ba7","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4666381.099874882,"y":5618342.996419203},{"fontSize":14,"id":"9335a836-2027-4198-9dac-44994cf16c5b","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4666747.928535348,"y":5618008.616144844},{"fontSize":14,"id":"723705be-3774-4d0f-82bd-235aa83326b1","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4667111.535641903,"y":5617667.734482449},{"fontSize":14,"id":"47417723-7a7a-40d5-a361-8e3628ecd920","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4667452.417304299,"y":5617338.215542133},{"fontSize":14,"id":"d4ef4c06-ce1c-405b-8718-ea9ad99566cf","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4666657.026758709,"y":5621315.168270081},{"fontSize":14,"id":"66462ef8-8ae0-4d54-a1b1-fed2fc9114f7","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4666997.908421105,"y":5621019.737496005},{"fontSize":14,"id":"15d66f64-9640-4099-8471-6e75c6bcae36","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4667384.2409718195,"y":5620690.21855569},{"fontSize":14,"id":"5c279b9e-9181-4e7b-a14d-f1b1e6254f47","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4667759.210800455,"y":5620360.699615374},{"fontSize":14,"id":"d46313b0-d754-4411-a374-bc53f73a3f4a","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4668156.90607325,"y":5620019.817952978},{"fontSize":14,"id":"78c81d90-f8f3-4692-a57e-555b71b2561b","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4668520.513179805,"y":5619713.024456822},{"fontSize":14,"id":"6a31c403-a8dd-4d25-8d50-2f21646965b7","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4664316.306010259,"y":5619292.603739868},{"fontSize":14,"id":"1ea62826-8f12-4daa-86ff-d5d9fbdb56d7","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4664657.187672655,"y":5618985.810243712},{"fontSize":14,"id":"980d3b53-b51f-4681-ab87-6672ad592c2c","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4664975.343890891,"y":5618667.6540254755},{"fontSize":14,"id":"5564996a-16c1-4452-bb15-c4a2a013ebd7","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4665304.862831207,"y":5618338.13508516},{"fontSize":14,"id":"7d99d894-0a8b-48be-a6c5-4db8ab76adee","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4665657.107215682,"y":5617974.527978605},{"fontSize":14,"id":"923c2f31-4834-44c2-af05-f729a681d9c1","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4666010.991356048,"y":5617620.644233307},{"fontSize":14,"id":"85af28e2-6626-4853-ba0d-7e88e71df8b5","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4666334.038209607,"y":5617305.737842623},{"fontSize":14,"id":"98a64612-2d77-448e-a0d3-0b5eff8c4e60","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4668634.140400603,"y":5621303.805548002},{"fontSize":14,"id":"90aa76fe-de94-43c9-a6af-fae823af7b1b","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4664418.570508978,"y":5616679.177661502},{"sourceID":"","id":"6adcd7f7-4130-420a-a08e-7312f2a03a98","title":"Бомба","x":4665086.321802849,"y":5621261.4788817065,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"91ea9735-17cd-4a79-b6e4-f34523d25320","title":"Бомба","x":4665436.473627751,"y":5620892.280193558,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"daff3ded-7d63-46b7-9290-2e3eb1fd2e96","title":"Бомба","x":4665654.805066216,"y":5620698.207803811,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"a830bb50-8a88-4074-aca2-ca40917969fe","title":"Бомба","x":4665994.431748272,"y":5620394.969694832,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"cec24d8b-2044-4691-ada5-0d88654af460","title":"Бомба","x":4666261.281284174,"y":5620091.731585853,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"61bb875b-5d3f-4f7d-a39d-2a01332cc25c","title":"Бомба","x":4666613.03749059,"y":5619788.493476874,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"fd9145be-78b6-4de9-958a-5d545e766f9f","title":"Бомба","x":4666952.664172646,"y":5619485.255367895,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"0bed382a-4490-49cc-ae3f-e16b7425c100","title":"Бомба","x":4667255.902281625,"y":5619169.887734557,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"189a655e-5f6c-4d66-bda0-cbe4c8240b7a","title":"Бомба","x":4667583.399439322,"y":5618842.390576859,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"b24a7652-9a69-4922-992b-db945b824d7c","title":"Бомба","x":4667983.673743174,"y":5618539.15246788,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"86cf77d7-d625-417d-977d-6c2391f441f4","title":"Бомба","x":4668299.0413765125,"y":5618175.266737105,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"339859a7-f70b-4110-8e66-2a889fa31e35","title":"Бомба","x":4668602.279485492,"y":5617847.769579408,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"73c85ef2-01bf-4294-bfab-24df80b2bc60","title":"Бомба","x":4668929.77664319,"y":5617508.142897352,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"36f237c5-cd34-428d-9a28-6882452f9a08","title":"Бомба","x":4669281.532849605,"y":5617156.386690935,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"1f098f1f-5e5d-4e62-a039-140268915c74","title":"Бомба","x":4664660.184068765,"y":5620601.171608938,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"2e934ca2-032f-4cf3-aa85-4c6218fd390e","title":"Бомба","x":4664878.515507229,"y":5620346.451597395,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"f95b7e41-65e3-4225-9061-ae646dc29c50","title":"Бомба","x":4665169.624091849,"y":5620115.990634571,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"d75eecd4-adf6-4602-bfae-3d8f52b02f3e","title":"Бомба","x":4665521.380298264,"y":5619655.068708923,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"b68b6ccb-6c12-4f36-b806-09101ff6f78d","title":"Бомба","x":4665836.747931602,"y":5619339.701075585,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"ed0e0b01-5b5a-49a9-a50e-dbe105b998a1","title":"Бомба","x":4666164.2450893,"y":5619024.333442247,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"e5f19d03-c7ad-4bf0-97d6-450d6d708606","title":"Бомба","x":4666467.4831982795,"y":5618830.2610524995,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"18ce38e0-6beb-4941-8ab6-d2ac4d2b62cf","title":"Бомба","x":4666843.498453413,"y":5618442.116273006,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"2f781b8c-cb89-48c6-bf9a-15401136f616","title":"Бомба","x":4667146.736562393,"y":5618138.878164028,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"3b29e9e2-d7a6-4cb3-abc9-814cadb2127d","title":"Бомба","x":4667534.881341886,"y":5617799.251481971,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"d6956674-182a-42e8-a189-8cb8486074c1","title":"Бомба","x":4664708.702166201,"y":5619412.47822174,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"50fc4b2f-379e-4b83-b970-0de2bc48a99f","title":"Бомба","x":4664405.464057222,"y":5619727.845855078,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"f251c616-bf7b-40d6-bedd-d1c528e9370d","title":"Бомба","x":4665060.458372616,"y":5619121.36963712,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"d28bef72-af8d-4817-b9d9-dabf68aaf815","title":"Бомба","x":4665351.566957236,"y":5618781.7429550635,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"dd10f92f-aa61-45df-b043-49375f941531","title":"Бомба","x":4665679.064114934,"y":5618417.857224288,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"9e2ea389-6878-4a6a-95a4-0c805f88430d","title":"Бомба","x":4666127.8565162225,"y":5618066.101017873,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"f590e96d-ca86-4117-8a13-93ed101d7161","title":"Бомба","x":4666431.094625202,"y":5617750.733384535,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"4c8f19e7-89fe-43be-a0b4-dcd459737f36","title":"Бомба","x":4666746.46225854,"y":5617423.236226837,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"6b0aeed1-92ba-4e84-bdd6-74e3b239c111","title":"Бомба","x":4666989.052745723,"y":5617132.127642217,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"faa6974c-f672-4d75-8c08-f71c5695bd88","title":"Бомба","x":4666249.1517598145,"y":5621438.10878972,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"b70e3afa-ed15-44e0-a1e6-014c093e7402","title":"Бомба","x":4666455.35367392,"y":5621013.575437149,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"97bf9b46-8ddd-45a8-aa12-f2f494429469","title":"Бомба","x":4666952.664172646,"y":5620673.948755093,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"2c9fc43e-e8d4-46e6-aa84-a419b591f96d","title":"Бомба","x":4667401.456573935,"y":5620358.581121755,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"aa159ee6-27a8-4885-86ae-26fc36b824ce","title":"Бомба","x":4667789.601353428,"y":5620043.213488416,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"eea0e7a9-de60-4f81-8af2-eb338a2a618f","title":"Бомба","x":4668092.839462407,"y":5619691.457282,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"7536f0fa-c6e5-4bdc-9a2a-50a489dbf35b","title":"Бомба","x":4668335.42994959,"y":5619363.960124303,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"bab4a4b4-efe7-4207-a6f6-0c1d2b54fb67","title":"Бомба","x":4668699.315680365,"y":5619121.36963712,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"84db962e-d03d-4749-91ac-afde8bf61a18","title":"Бомба","x":4669038.942362422,"y":5617896.287676845,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"d89f8653-218c-46d8-913a-86ddd2a9f0fa","title":"Бомба","x":4667935.155645738,"y":5617350.459080682,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"b91d12a1-6c39-44c3-96d2-90c9898cdcd7","title":"Бомба","x":4668323.300425231,"y":5621195.518302537,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"4fc916bf-000c-440c-a601-7fc2e26a8e2d","title":"Бомба","x":4668675.056631647,"y":5620916.539242276,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"5bba6238-939e-4196-bc58-bdf47bd1e373","title":"Бомба","x":4664526.759300813,"y":5617059.350496062,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"7e314fe8-ee4a-4a45-a6fd-1e82244160d0","title":"Бомба","x":4664866.38598287,"y":5616780.3714358015,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"0759abcb-0a3b-4a36-82e6-08892a6fa47a","title":"Бомба","x":4667947.285170097,"y":5620855.89162048,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"},{"sourceID":"","id":"6d3bdeeb-94db-4bda-b3f2-57f679a1c33a","title":"Бомба","x":4668286.911852154,"y":5620504.135414064,"locked":False,"type":"static_icon","fontSize":14,"sourceType":"static_icon","polygon":[],"schemaName":"icon_bomb"}],"sxfMaps":{"apiUrl":"http://10.201.0.1:5634","layerIds":[]}}}
        requests.put(self.url+'/api/data/system/zone/'+self.get_zone(), headers=self.get_token(), json=body, verify=False)
        yn = input('Удалить добавленные элементы?(y/n): ')
        if yn =='y' or 'Y' or 'yes' or 'YES' or 'Yes':
            self.del_targets()


    def rand_targets(self,ns):
        block_b = '{"fontSize":14,'+f'"id":"{self.rand_id()}"'+',"locked":false,"polygon":[],'+f'"schemaName":"{self.rand_icon()}",'+'"sourceID":"","sourceType":"static_icon","title":"Тестовый объект'f'{ns}'+'","type":"static_icon",'+f'"x":{self.rand_x()},"y":{self.rand_y()}'+'},'
        
        return (block_b)

        
    def add_99_targets(self):
            warnings.filterwarnings('ignore')
            os.system('cls' if os.name == 'nt' else 'clear')
            self.del_targets()

            block_open = '{"title":"Murom","settings":{"backgroundImage":"","items":[{"fontSize":0,"id":"946aa060-24ae-11ef-b321-c905af5a3e46","locked":false,"polygon":[],"sourceID":"","sourceType":"murom","title":"Комплекс Муром-П","type":"icon","x":41.920834,"y":44.983891},'
            
            block_close = '{"fontSize":14,"id":"628745aa-7aae-435b-bed9-130c4fb3b65d","locked":false,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Тестовый объект","type":"static_icon","x":4664668.550394735,"y":5621110.639272644}],"sxfMaps":{"apiUrl":"http://10.201.0.1:5634","layerIds":[]}}}'
            
            i = input ('Сколько объектов требуется?: ')
            many_blocks = ''
            for ns in range(int(i)):
                many_blocks = many_blocks + self.rand_targets(ns)
            
            body = json.loads(block_open + many_blocks + block_close) 
            resp = requests.put('https://gate.synerget.ru:8179/api/data/system/zone/'+self.get_zone(), headers=self.get_token(), json=body, verify=False)
            print(resp)
            yn = input('Удалить объекты с план-схемы?(y/n): ')
            if yn =='y':
                self.del_targets()
            else:
                return('no del')
            

    def del_targets(self):
        
        body ={"title":"Murom","settings":{"backgroundImage":"Custom:http://10.201.0.1:13370","items":[{"fontSize":0,"id":"2cb06ef0-dcf2-11ed-b84f-07d68e1078e7","locked":False,"polygon":[],"sourceID":"","sourceType":"murom","title":"Комплекс Муром-П","type":"icon","x":41.921112,"y":44.983612}],"sxfMaps":{"apiUrl":"http://10.201.0.1:5634","layerIds":[]}}}
        
        requests.put('https://gate.synerget.ru:8179/api/data/system/zone/'+self.get_zone(), headers=self.get_token(), json=body, verify=False)


    def del_panorama(self):
        body = {"image": ""}
        requests.post(self.url+'/api/data/ui/panorama', headers=self.get_token(), json=body, verify=False)    
       

