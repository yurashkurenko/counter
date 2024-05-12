import socket
import ujpeg
import os

# настройка Telegram
TELEGRAM_TOKEN = "YOUR_TELEGRAM_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

# настройка Socket
SOCKET_ADDRESS = ("api.telegram.org", 443)
SOCKET_PORT = 443

# функция для отправки фото в Telegram
def send_photo(photo_path):
    # отправляем запрос на сервер Telegram
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SOCKET_ADDRESS, SOCKET_PORT))

    # отправляем запрос на отправку фото
    request = f"POST /bot{TELEGRAM_TOKEN}/sendPhoto HTTP/1.1\r\n"
    request += f"Host: {SOCKET_ADDRESS}\r\n"
    request += f"Content-Type: application/x-www-form-urlencoded\r\n"
    request += f"Content-Length: {len(request)}\r\n\r\n"
    request += f"chat_id={TELEGRAM_CHAT_ID}&photo=@{photo_path}"

    sock.sendall(request.encode())

    # получаем ответ от сервера Telegram
    response = sock.recv(1024).decode()
    print(response)

    # закрываем соединение
    sock.close()

# пример использования функции
photo_path = "path/to/your/image.jpg"
send_photo(photo_path)
