import requests
import allure
from ApiRes import ApiRes
import warnings




@allure.epic('MUROM')
class MuromTest:
    #pytest --alluredir=D:/allure/allure_results
    #allure serve D:/allure/allure_results  

    base_url = 'https://gate.synerget.ru:8179'
    api = ApiRes(base_url)
    
    @allure.severity('critical')
    @allure.feature('api тесты')
    @allure.story('Тест модулей')
    @allure.title('Получение списка модулей')
    def test_create_com(self):
        warnings.filterwarnings('ignore')
        with allure.step('Получить список модулей из system/module'):       
            resp = requests.get(self.base_url+'/api/data/system/module', headers=self.api.get_token(), verify=False)
            
        with allure.step('Сравнить статус код списка модулей с статус кодом 200'):
            assert resp.status_code == 200