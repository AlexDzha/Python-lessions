Special_Symbols = ['!','@','#','$','%','^','&','*','(',')','_','-','=','+','<','>','?']
bad_password = ('Пароль должен удовлетворять следующим условиям:'
                  '\n1) Длина пароля должна быть от 8 до 20 символов;'
                  '\n2) Пароль должен содержать минимум 1 число;'
                  '\n3) Пароль должен содержать минимум 1 заглавную букву'
                  '\n4) Пароль должен содержать минимум 1 строчную букву'
                  '\n5) Пароль должен содержать минимум 1 специальный символ.')
class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password
class User:
    """

Класс пользователя, содержащий атрибуты: логин и пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input("Приветствую! Выберите действие: \n1 - вход\n2 - Регистрация\n"))
        if choice == 1:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}')
                else:
                    print('Неверный пароль')
            else:
                print("Пользователь не найден.")
        if choice == 2:
            user = User(input("Введите логин: "), password := input("Введите пароль: "),
                        password2 := input("Повторите пароль: "))
            if len(password) <8 or len(password) >20:
                print(bad_password)
                continue
            elif not any(char.isdigit() for char in password):
                print(bad_password)
                continue
            elif not any(char.isupper() for char in password):
                print(bad_password)
                continue
            elif not any(char.islower() for char in password):
                print(bad_password)
                continue
            elif not any(char in Special_Symbols for char in password):
                print(bad_password)
                continue
            elif password != password2:
                print('Введенные пароли не совпадают, попробуйте еще раз.')
                continue

            database.add_user(user.username, user.password)
        print(database.data)
