from smartphone import Smartphone

catalog = []

catalog.append(Smartphone('Nokia', '3310', '8 800 999 00 11'))
catalog.append(Smartphone('Alkatel', 'OT-222', '8 800 753 12 21'))
catalog.append(Smartphone('Sony', 'Walkman Z', '8 928 928 92 89'))
catalog.append(Smartphone('HTC', 'One', '8 918 918 91 89'))
catalog.append(Smartphone('Samsung', 'C 100', '8 999 888 77 66'))

for i in catalog:
    print(f'{i.mark} - {i.model}. {i.number}')
 
