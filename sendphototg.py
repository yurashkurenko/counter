import requests
from settings import TOKEN,CHATID
def send_photo(chat_id, photo_path, token):
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    with open(photo_path, 'rb') as photo:
        files = {'photo': photo}
        data = {'chat_id': chat_id}
        r = requests.post(url, files=files, data=data)
        return r.json()

# Использование
if __name__ == '__main__':
#    TOKEN = 'your_bot_token_here'
#   CHATID = 'your_chat_id_here'
    IMAGE_TEXT = 'Hello, Telegram!'
    IMAGE_FILENAME = 'image_with_text.png'

    # Создаем изображение с надписью
#    create_image_with_text(IMAGE_TEXT, IMAGE_FILENAME)

    # Отправляем изображение
    result = send_photo(CHATID, IMAGE_FILENAME, TOKEN)
    print(result)
