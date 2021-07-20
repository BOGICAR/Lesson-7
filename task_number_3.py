# Задание №3 - сделано
import requests
import datetime

API_KEY = 'f9ada9efec6a3934dad5f30068fdcbb8'
u_input_city = input()
u_unput_days = input()


def openweathermap():
    get_data = requests.get(f'http://api.openweathermap.org/data/2.5/forecast/daily?',
                            params={'q': u_input_city,
                                    'cnt': u_unput_days,
                                    'units': 'metric',
                                    'appid': API_KEY})
    return get_data.json()


def format_list():
    x = openweathermap()
    list_1 = []
    for day in x['list']:
        list_2 = []
        datetime_ = datetime.datetime.fromtimestamp(day['dt'])
        format_datetime_ = datetime_.strftime('%d-%m-%Y')
        list_2.append(str(format_datetime_))
        list_2.append(str(day['temp']['day']))
        list_2.append(str(day['feels_like']['day']))
        list_2.append(str(day['temp']['night']))  # Доп: колонка Температура ночью
        list_1.append(list_2)
    return list_1


def file_name():
    x = format_list()
    datetime_1 = datetime.datetime.now().date()
    with open(f'{datetime_1}-{u_input_city}-{u_unput_days}-days-weather-forecast.txt', 'w') as file:
        file.write('Date'.ljust(20) + 'Day Temperature'.ljust(20) + 'Feels Like'.ljust(20) +
                   'Temperature at night'.ljust(20) + '\n')
        for line in x:
            for i, val in enumerate(line):
                line[i] = val.ljust(20)
            file.write(''.join(line) + '\n')


file_name()
