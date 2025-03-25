from faker import Faker

class Generator:
    fake = Faker()

    @staticmethod
    def fake_login():
        return Generator.fake.user_name()

    @staticmethod
    def fake_password():
        return Generator.fake.password()

    @staticmethod
    def fake_first_name():
        return Generator.fake.first_name()