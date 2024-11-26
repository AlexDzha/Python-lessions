import requests

# 1. Отправляем GET-запрос к сайту
url = 'https://dnd.su/'
response = requests.get(url)

# 2. Проверяем статусный код ответа
if response.status_code == 200:
    print("Запрос успешен. Код ответа:", response.status_code)
else:
    print("Ошибка в запросе. Код ответа:", response.status_code)

# 3. Получаем содержимое страницы
content = response.text
print("Содержимое страницы:", content[:500])  # Выводим первые 500 символов

# 4. Выводим заголовки ответа
print("Заголовки ответа:")
for key, value in response.headers.items():
    print(f"{key}: {value}")

# 5. Также можно работать с параметрами запроса
params = {'key': 'value'}  # Пример параметров
response_with_params = requests.get(url, params=params)
print("Ответ с параметрами:", response_with_params.status_code)
