from faker import Faker

class Data:
    fake = Faker()
    login = fake.user_name()
    password = fake.password()
    firstName = fake.name()
    login_exist = fake.user_name()
    password_exist = fake.password()
    firstName_exist = fake.name()