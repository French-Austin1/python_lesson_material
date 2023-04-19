import random


class Person:
    def __init__(self, f_name, l_name, age, phone_num = None, email = None) -> None:
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        if phone_num:
            self.phone_num = phone_num
        else:
            self.phone_num = self._generate_random_phonenumber()
        if email:
            self.email = email
        else:
            self.email = self._generate_email()

    def _generate_random_phonenumber(self):
        '''Generate a random phone number with 10 digits and a 555 area code'''
        return f'555-{random.randint(100,999)}-{random.randint(1000,9999)}'

    def _generate_email(self):
        '''Generate an email address from the first and last name'''
        return self.l_name.lower() + "." + self.f_name.lower() + '@mysite.com'
    
    def get_name(self):
        return self.f_name + " " + self.l_name
    
    def get_age(self):
        return self.age
    
    def get_phone_num(self):
        return self.phone_num
    
    def get_email(self):
        return self.email
    
    def get_id(self):
        '''Return a formatted representation of the Person object and its attributes'''
        return f'{self.get_name()} is {self.get_age()} years old and can be reached at {self.get_phone_num()} or {self.get_email()}'