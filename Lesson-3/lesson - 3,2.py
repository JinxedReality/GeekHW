# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def print_data(name, surname, birthday, city, email, phone):
    return f'Name - {name}, surname - {surname}, birthday - {birthday}, city - {city}, 'f'email - {email}, phone - {phone}'


print(print_data(name='Влад', surname='Колков', birthday='24.11.1997', city='Люберцы', email='none@null.net',
                 phone='+4-815-16-23-42'))
