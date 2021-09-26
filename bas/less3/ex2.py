#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
#Функция должна принимать параметры как именованные аргументы.
#Реализовать вывод данных о пользователе одной строкой.

def print_user_file(**file) -> None:
    print(f'Имя: {file.get("name")}, '
          f'Фамилия: {file.get("surname")},'
          f'Год рождения: {file.get("birth_year")}, '
          f'Город проживания: {file.get("city")},'
          f'email: {file.get("email")}, '
          f'Телефон: {file.get("phone")}')
if __name__ == '__main__':
    user = {
        'name': 'Дарья',
        'surname': 'Иванова',
        'birth_year': '1994',
        'city': 'Москва',
        'email': 'darya1994@mail.ru',
        'phone': '466-33-22',
    }
 #   print(f'{user}')
    print_user_file(**user)
