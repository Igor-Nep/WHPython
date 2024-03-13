class User:
    
    def __init__(self, first_name, last_name):
        self.user_name = first_name
        self.user_last_name = last_name

    def print_name(self):
        print(f'Ваше имя: {self.user_name}')

    def print_last_name(self):
        print(f'Ваша фамилия: {self.user_last_name}') 

    def print_full_name(self):
        print(f'Ваше полное имя: {self.user_name} {self.user_last_name}')       


