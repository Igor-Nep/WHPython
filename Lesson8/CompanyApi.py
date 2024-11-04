import requests
class CompanyApi:

    def __init__(self, url):
        self.url = url

    def get_company_list(self, params_to_add = None):
        resp = requests.get(self.url +'/company',params=params_to_add)
        return resp.json() 

    def get_token(self, user = 'raphael', password = 'cool-but-crude'):
        creds = {
            'username': user,
            'password': password
            }
        resp = requests.post(self.url +'/auth/login', json=creds)
        return resp.json()["userToken"] 

    def create_company(self, name, description = ''):
        company ={
            "name": name,
            "description": description
            }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token() 
        create = requests.post(self.url +'/company', json=company, headers=my_headers)
        return create.json()  
    
    def get_company(self, id):
         resp = requests.get(self.url +'/company/'+str(id))
         return resp.json()


    def edit(self, new_id, new_nam, new_des):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token() 
        company ={
            "name": new_nam,
            "description": new_des
            }
        resp = requests.patch(self.url +'/company/'+str(new_id),headers=my_headers, json=company)
        return resp.json()
        

    def del_company(self, id):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token() 
       
        resp = requests.get(self.url +'/company/delete/'+str(id),headers=my_headers)
        return resp.json()

    def deactivate(self, id, isActive):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url +'/company/status/'+str(id), headers=my_headers, json={'isActive': isActive})

        return resp.json()

        