import requests


def get_vacancies_amount(keywords_string: str) -> dict:
    _url = 'https://api.rabota.ua/vacancy/search'
    _params = {"keywords": keywords_string}
    try:
        response = requests.get(url=_url, params=_params)
    except requests.ConnectionError:
        return {"error": "Problem with request. Check your internet connection or Provided url"}

    if not response.json()['documents']:
        return {"error": "There is no any vacancies by this keyword"}

    if response.status_code == 200:
        vacancies_amount = response.json()['total']
        return {"success": vacancies_amount}

    if 400 <= response.status_code < 500:
        return {"error": f"Client error. {response.reason}"}

    if response.status_code >= 500:
        return {"error": "Service unavailable. Try again later"}
    return {"error": "Unexpected behavior"}


if __name__ == '__main__':
    url = 'https://api.rabota.ua/vacancy/search'
    keywords = "junior"
    result = get_vacancies_amount(keywords)
    print(result)

