from address import Address
from mailing import Mailing

address_from = Address('555000', 'Москва', 'Ленина', '100', '10')
address_to = Address('777000', 'Санкт-Петербург', 'Мира', '10', '100')

tracking_1 = Mailing(address_to, address_from, 1500, '17665540')

print(f'Отправление номер {tracking_1.track} '
            f'из {tracking_1.from_address.index} '
            f'{tracking_1.from_address.city}, '
            f'улица {tracking_1.from_address.street} '
            f'{tracking_1.from_address.house}, '
            f'кв.{tracking_1.from_address.flat}'
            f' в {tracking_1.to_address.index}'
            f' {tracking_1.to_address.city}, '
            f'улица {tracking_1.to_address.street}'
            f' {tracking_1.to_address.house} '
            f'кв.{tracking_1.to_address.flat}. '
            f'Стоимость {tracking_1.cost} рублей.')

