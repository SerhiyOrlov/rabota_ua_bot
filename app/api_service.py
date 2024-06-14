import requests

# URL стороннего API
url = 'https://api.rabota.ua/vacancy/search'
params = {"keywords": "junior"}

def get_vacancies_amount(url, params):
    # Выполнение GET-запроса
    response = requests.get(url, params=params)

    # Проверка успешности запроса
    if response.status_code == 200:
        # Парсинг JSON-ответа
        data = response.json()
        print(data['total'])
    else:
        print(f"Ошибка: {response.status_code}")

