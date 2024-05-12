import socket
#import ujpeg
import os
#import netphone

from settings import TOKEN, CHATID
# настройка Telegram
#TELEGRAM_TOKEN = "YOUR_TELEGRAM_TOKEN"
#TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"
TELEGRAM_TOKEN = TOKEN
TELEGRAM_CHAT_ID = CHATID
# настройка Socket
SOCKET_ADDRESS = "api.telegram.org"
SOCKET_PORT = 443

# функция для отправки фото в Telegram
def send_photo():
# отправляем запрос на сервер Telegram
#    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    print(fbuf)
    sock = socket.socket()
    sock.connect(socket.getaddrinfo(SOCKET_ADDRESS, SOCKET_PORT)[0][-1])
    # отправляем запрос на отправку фото
    request = f"POST /bot1701291551:AAEk2TbH7mbHLPVVBrP0gEOSZBezbjH1FHY/sendPhoto HTTP/1.1\r\n"
    request += f"Host: api.telegram.org\r\n"
    request += f"User-Agent: python-requests/2.31.0\r\n"
    request += f"Accept-Encoding: gzip, deflate"
    request += f"\r\nAccept: */*\r\n"
    request += f"Connection: keep-alive\r\nContent-Length: 12052\r\n"
    request += f"Content-Type: multipart/form-data; boundary=97d81ac404017fec19458e34bae65b01\r\n\r\n"
    request += f"--97d81ac404017fec19458e34bae65b01\r\n"
    request += f"Content-Disposition: form-data; name=\"chat_id\"\r\n\r\n"
    request += f"159085018\r\n"
    request += f"--97d81ac404017fec19458e34bae65b01\r\n"
    request += f"Content-Disposition: form-data; name=\"photo\"; filename=\"Magic_Poser.jpg\"\r\n\r\n"
    request += str(open("foto.jpg", "rb"))
    request += f"\r\n--97d81ac404017fec19458e34bae65b01--\r\n"
    print(len(request))
    print(len(open("foto.jpg", "rb")))
    sock.sendall(request) 
#    print(request)
    response = sock.recv(1024).decode()
    print(response)
    # закрываем соединение
    sock.close()

# пример использования функции

send_photo()
