import requests
import json


def get_api_data(kfc_api_url):
    # Отправляем GET-запрос к API
    response = requests.get(kfc_api_url)

    # Проверяем успешность запроса (код ответа 200)
    if response.status_code == 200:
        # Преобразуем данные в формат JSON
        json_data = response.json()
        return json_data
    else:
        # Если запрос неудачен, выведите сообщение об ошибке
        print(f"Ошибка при запросе API. Код ответа: {response.status_code}")
        return None


def save_json_data(data, output_file):
    # Сохраняем данные в файл в формате JSON
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


# Наш api, который получили с сайта
api_url = 'https://api.prod.digital.uni.rest/api/store/v2/store.get_restaurants?showClosed=true'

# Получаем данные из API
api_data = get_api_data(api_url)

# Сообщение об успешном импорте
if api_data:
    save_json_data(api_data, 'kfc.json')
    print("Данные успешно сохранены в файл 'kfc.json'")
