import json
import sqlite3

# Загрузка JSON файла
with open('kfc.json', 'r', encoding='windows-1251') as json_file:
    data = json.load(json_file)

# Подключение к базе данных SQLite
conn = sqlite3.connect('kfc_data.db')
cursor = conn.cursor()

# Создание таблицы, если её нет
cursor.execute('''
    CREATE TABLE IF NOT EXISTS store_info (
        street_address_ru TEXT,
        city_ru TEXT,
        coordinates_X REAL,
        coordinates_Y REAL,
        opening_hours_start_time TIME,
        opening_hours_end_time TIME,
        menu_start_time TIME,
        menu_end_time TIME
    )
''')

# Извлечение и вставка данных для каждого объекта в массиве searchResults
for result in range(len(data["searchResults"])):
    # Проверка на пустые поля в адресе ресторана
    try:
        street_address_ru = data["searchResults"][result]["storePublic"]["contacts"]["streetAddress"]["ru"]
    except KeyError:
        street_address_ru = None

    city_ru = data["searchResults"][result]["storePublic"]["contacts"]["city"]["ru"]
    coordinates_X = (data["searchResults"][result]["storePublic"]["contacts"]["coordinates"]["geometry"]["coordinates"][0])
    coordinates_Y = (data["searchResults"][result]["storePublic"]["contacts"]["coordinates"]["geometry"]["coordinates"][1])
    opening_hours_start_time = data["searchResults"][result]["storePublic"]["openingHours"]["regular"]["startTimeLocal"]
    opening_hours_end_time = data["searchResults"][result]["storePublic"]["openingHours"]["regular"]["endTimeLocal"]

    # Проверка наличия меню
    if data["searchResults"][result]["storePublic"]["menues"]:
        menu_start_time = data["searchResults"][result]["storePublic"]["menues"][0]["availability"]["regular"]["startTimeLocal"]
        menu_end_time = data["searchResults"][result]["storePublic"]["menues"][0]["availability"]["regular"]["endTimeLocal"]
    else:
        menu_start_time = menu_end_time = None

    # Вставка данных в таблицу
    cursor.execute('''
        INSERT INTO store_info
        (street_address_ru, city_ru, coordinates_X, coordinates_Y, opening_hours_start_time, opening_hours_end_time, menu_start_time, menu_end_time)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (street_address_ru, city_ru, coordinates_X, coordinates_Y, opening_hours_start_time, opening_hours_end_time, menu_start_time, menu_end_time))

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
