#import http.client as http_client
#import logging
import urequests as requests
#http_client.HTTPConnection.debuglevel = 1

def send_photo(token, chat_id, photo_path, caption):
  url = f'https://api.telegram.org/bot{token}/sendPhoto'
  with open(photo_path, 'rb') as photo:
    headers={"Content-Type": "multipart/form-data; boundary=97d81ac404017fec19458e34bae65b01"}
    data=b'--97d81ac404017fec19458e34bae65b01\r\nContent-Disposition: form-data; \
    name="chat_id"\r\n\r\n159085018\r\n--97d81ac404017fec19458e34bae65b01\r\n \
    \r\nContent-Disposition: form-data; name="caption"\r\n\r\n'+caption+ \
    b'\r\n--97d81ac404017fec19458e34bae65b01\r\n \
    Content-Disposition: form-data; name="photo"; filename="image.jpg"\r\n\r\n'
    print(data)
    f=open(photo_path,"rb")
    imgbstr=f.read()
    f.close()
    data=data+imgbstr+b'\r\n--97d81ac404017fec19458e34bae65b01--\r\n\r\n'
    r = requests.post(url,headers=headers,data=data)
  return r.json()
# Функция отправки картинки с заголовком_____________   
#if __name__ == 'main':
