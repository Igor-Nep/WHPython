
import requests
base_url=('https://x-clients-be.onrender.com')


def get_token(user = 'raphael', password = 'cool-but-crude'):
    creds = {
            'username': user,
            'password': password
            }
    resp = requests.post(base_url +'/auth/login', json=creds)
    return resp.json()["userToken"] 
    
def create_company(name, desc = ''):
    company ={
            "name": name,
            "description": desc
            }
    header = {}
    header["x-client-token"] = get_token() 
    create = requests.post(base_url +'/company', json=company, headers=header)
    return create.json()

def create_employee():
    body = {
        "id": 0,
        "firstName": "Igor",
        "lastName": "string",
        "middleName": "string",
        "companyId": 3145,
        "email": "vomiterpen@gmail.com",
        "url": "string",
        "phone": "string",
        "birthdate": "2024-05-22T19:58:40.096Z",
        "isActive": True
        }
    header = {}
    header["x-client-token"] = get_token() 
    create = requests.post(base_url +'/employee', json=body, headers=header)
    return create.json()
    
       
n = create_employee()
print(n)