from faker import Faker

class Data:
    fake = Faker()
    login = fake.user_name()
    password = fake.password()
    firstName = fake.name()
    login_exist = fake.user_name()
    password_exist = fake.password()
    firstName_exist = fake.name()

    create_courier_400_error = "Недостаточно данных для создания учетной записи"
    create_courier_409_error = "Этот логин уже используется. Попробуйте другой."
    login_404_error = "Учетная запись не найдена"
    login_400_error = "Недостаточно данных для входа"

    order_data = [("Саша", "Пушкин", "ул. Мира, д. 3", 4, "+7 800 355 35 35", 5, "2025-03-30", "тест", ["BLACK"]),
     ("Саша", "Пушкин", "ул. Мира, д. 3", 4, "+7 800 355 35 35", 5, "2025-03-30", "тест", ["GREY"]),
     ("Саша", "Пушкин", "ул. Мира, д. 3", 4, "+7 800 355 35 35", 5, "2025-03-30", "тест", ["BLACK", "GREY"]),
     ("Саша", "Пушкин", "ул. Мира, д. 3", 4, "+7 800 355 35 35", 5, "2025-03-30", "тест", [])]