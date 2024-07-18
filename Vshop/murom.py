from ApiRes import ApiRes
import random
import requests
api = ApiRes('https://gate.synerget.ru:8179')

#api.start()



#{"title":"Murom","settings":{"backgroundImage":"","items":[
#{"fontSize":0,"id":"946aa060-24ae-11ef-b321-c905af5a3e46","locked":False,"polygon":[],"sourceID":"","sourceType":"murom","title":"Комплекс Муром-П","type":"icon","x":41.920834,"y":44.983891},
# {"fontSize":14,"id":"628745aa-7aae-435b-bed9-130c4fb3b65d","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":4664668.550394735,"y":5621110.639272644},
# {"fontSize":14,"id":"65467d95-88e5-4904-a20e-f1c25d672629","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon",
#],"sxfMaps":{"apiUrl":"http://10.201.0.1:5634","layerIds":[]}}}

#"x":4664668.550394735,"y":5621110.639272644
#"x":4668092.839462407,"y":5619691.457282
#"x":4667401.456573935,"y":5620358.581121755
#"x":4666952.664172646,"y":5620673.948755093
#"x":4664878.515507229,"y":5620346.451597395
#"x":4667583.399439322,"y":5618842.390576859
#"x":4667983.673743174,"y":5618539.15246788
x1 = '46'.join([random.choice('67895432') for _ in range(5)])
x2_1 = ''.join([random.choice('678954') for _ in range(2)])
x2_2 = x2_1.join([random.choice('678954321') for _ in range(5)])
x = f'{x1}.{x2_1}{x2_2}'

y1 = '56'.join([random.choice('67895432') for _ in range(5)])
y2_1 = ''.join([random.choice('678954') for _ in range(2)])
y2_2 = x2_1.join([random.choice('678954321') for _ in range(5)])
y = f'{y1}.{y2_1}{y2_2}'


b1 = '{"title":"Murom","settings":{"backgroundImage":"","items":['
#b2 = '{'+f'"fontSize":14,"id":"{api.generate_id()}","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":{x},"y":{y}'
item = ''

for _ in range(0, 10):
    #item = item + f'"fontSize":14,"id":"{b_id}","locked":False,"polygon":[],"schemaName":"icon_plane","sourceID":"","sourceType":"static_icon","title":"Самолет","type":"static_icon","x":{x},"y":{y}'
    print(x)
    print(y)
    