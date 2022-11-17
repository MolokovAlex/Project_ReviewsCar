import requests

url = 'http://localhost:8000/api/country/'  # Полный адрес эндпоинта
response_in_json = requests.get(url)  # Делаем GET-запрос
# Поскольку данные пришли в формате json, переведем их в python
response_in_python = response_in_json.json()
# Запишем полученные данные в файл capitals.txt
with open('country.txt', 'w') as file:
    for item_country in response_in_python:
        file.write(
            f"Name of country {item_country['country_name']} \n"
        )