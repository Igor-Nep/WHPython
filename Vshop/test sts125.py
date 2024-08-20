import threading
from time import sleep
import requests
from datetime import datetime
import msgpack
import os

URL_ADDRESS = "http://192.168.65.56:8089"

# filter module list
def filtered_modules():
    response = requests.post(URL_ADDRESS +'/api/data/system/module/list?subsystem=security')
    data = response.json()
    filtered_modules = {}
    # list of all security subsystem
    for key in data['data']:
        filtered_modules[key['id']] = key['title']
    return filtered_modules

def module_state(thread_number,filtered_modules):
    path_to_script = os.path.dirname(os.path.abspath(__file__))
    my_filename = os.path.join(path_to_script, 'thread'+str(thread_number)+'.txt')
    # cycle count
    for i in range(20):
        with open(my_filename, 'a') as f:
            print('STEP ', str(i), file=f)
        sleep(1)
        for key, value in filtered_modules.items():
            # ModuleStateRequest
            response = requests.post(URL_ADDRESS +'/api/modules/'+ key +'/ModuleStateRequest')
            # GetState
            header = {'Content-Type':'application/msgpack'}
            # send binary data
            data = msgpack.packb(0, use_bin_type=True)
            get_state = requests.post(URL_ADDRESS +'/api/modules/'+ key +'/Security/GetState', headers=header, data=data)
            # txt output
            with open(my_filename, 'a') as f:
                print(str(datetime.now()),' ',str(key),' ', str(value),' ',str(msgpack.unpackb(response.content, strict_map_key=False)),' ',str(msgpack.unpackb(get_state.content, strict_map_key=False)[0]), file=f)
            get_state.close
            response.close

# SetOffGuard 
# SetOnGuard
def module_set_state(state):
    for key, value in filtered_modules().items():
        header = {'Content-Type':'application/msgpack'}
         # send binary data
        data = msgpack.packb(0, use_bin_type=True)
        requests.put(URL_ADDRESS +'/api/modules/'+ key +'/Security/'+ state, headers=header, data=data)
        sleep(.01)
        get_state = requests.post(URL_ADDRESS +'/api/modules/'+ key +'/Security/GetState', headers=header, data=data)
        response = requests.post(URL_ADDRESS +'/api/modules/'+ key +'/ModuleStateRequest')
        print(value, *msgpack.unpackb(get_state.content, strict_map_key=False)[0], msgpack.unpackb(response.content, strict_map_key=False))

# multi threading
if __name__ == '__main__':
    flt = filtered_modules()
    # for multi threading change number in range
    for i in range(1):
         my_thread = threading.Thread(target=module_state, args=(i,flt))
         my_thread.start()


#module_set_state('SetOnGuard')

