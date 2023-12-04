import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('kfc_data.db')
cursor = conn.cursor()

# Запрос из задания
query = """
    SELECT street_address_ru
    FROM store_info
    WHERE city_ru = 'Новосибирск'
      AND opening_hours_start_time <= '08:45:00'
      AND menu_start_time <= '08:45:00'
      AND menu_end_time >= '08:45:00';
"""

# Выполнение запроса
cursor.execute(query)

# Получение результатов
results = cursor.fetchall()

# Вывод результатов
for result in results:
    print(result[0])

# Закрытие соединения
conn.close()
