# 2. Выполнить функцию, которая принимает несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания, email,
# телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def person(name, sec_name, age, city, email, tel):
    return f'Имя - {name}, фамилия - {sec_name}, год рождения - {age}, город проживания - {city}, ' \
           f'email - {email}, телефон {tel}'


name = input('Введите имя: ')
sec_name = input('Введите Фамилию: ')
age = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите email:')
tel = input('Введите телефон: ')

print(person(name, sec_name, age, city, email, tel))