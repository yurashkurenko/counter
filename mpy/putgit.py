import requests

# Данные для аутентификации на GitHub
username = 'ваше_имя_пользователя'
token = 'ваш_токен_доступа'

# Репозиторий и путь к файлу на GitHub
repo = 'имя_репозитория'
path = 'путь/к/файлу.txt'

# Содержимое файла
file_content = 'Текст, который нужно загрузить'

# URL для доступа к API GitHub
url = f'https://api.github.com/repos/{username}/{repo}/contents/{path}'

# Заголовки запроса
headers = {
    'Authorization': f'token {token}',
    'Content-Type': 'application/json'
}

# Данные для отправки в запросе
data = {
    'message': 'Загрузка файла',
    'content': file_content
}

# Отправка PUT-запроса на GitHub API
response = requests.put(url, headers=headers, json=data)

# Проверка статуса ответа
if response.status_code == 201:
    print('Файл успешно загружен на GitHub')
else:
    print('Ошибка при загрузке файла:', response.text)
