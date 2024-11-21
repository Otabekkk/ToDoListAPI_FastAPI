from pydantic import BaseModel, EmailStr

class Credentials(BaseModel):
    email: EmailStr
    password: str

class User(BaseModel):
    creds: Credentials
    name: str

class NewUser(Credentials):
    name: str

if __name__ == '__main__':
    user = User(creds = Credentials(email = 'Amanismailov@gmail.com', password = 'pass'), name = 'Aman')
    user_new = NewUser(email = 'Amanismailov@gmail.com', password = 'pass', name = 'Alex')
    print(user.creds)
    print(user_new.password)
