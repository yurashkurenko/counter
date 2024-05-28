import requests

# Указываем URL сервера, к которому обращаемся
url = 'http://127.0.0.1:5005/devpara'

# Задаём device_id, который хотим запросить
device_id = ''

# Создаём словарь с данными, которые будут отправлены в POST-запросе
data = { 'device_id': device_id }

# Дополнительно можно задать заголовки, если API требует их наличие
headers = { 'Content-Type': 'application/json' }
#    ,
#    'Authorization': 'Bearer your_token_here'  # Пример токена, если нужна авторизация
#}

# Отправляем POST-запрос
response = requests.post(url, json=data, headers=headers)

# Пров&еряем статус ответа
if response.status_code == 200:
    # Выводим результат запроса, если ответ успешный
    print("Response from server:", response.json())
else:
    # Выводим сообщение об ошибке, если запрос не прошёл
    print("Failed to get device parameters. Status code:", response.status_code)