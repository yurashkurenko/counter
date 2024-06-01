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
# _____________                                                                                                                                                                                          #if __name__ == 'main':
from settings import TOKEN,CHATID
IMAGE_FILENAME = 'girl.jpg'
CAPTION=b'Hello-hello\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82 \
\xd0\xb8\xd0\xb7\xd0\xb3\xd0\xbb\xd1\x83\xd0\xb1\xd0\xb8\xd0\xbd\xd1\x8b \
\xd0\xb2\xd1\x81\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb9\r\n'
# __________ ___________                                                                                                                                                                                 print('123...')
result = send_photo(TOKEN, CHATID, IMAGE_FILENAME, CAPTION)
#print(result)
