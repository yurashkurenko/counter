import http.client as http_client         
import logging                            
import requests                           
http_client.HTTPConnection.debuglevel = 1                                           
from settings import TOKEN,CHATID         
def send_photo(chat_id, photo_path, token):                                             
  url = f'https://api.telegram.org/bot{token}/sendPhoto'                              
  with open(photo_path, 'rb') as photo:         
    files = {'photo': photo}                  
#    data = {'chat_id': chat_id}
#    data = {'chat_id': chat_id,'img': base64.b64encode(image_data).decode('ascii'),'caption': 'картинка в телеграме'}
    data = {'chat_id': chat_id,'caption': 'картинка в телеграме'}
    r = requests.post(url, files=files, data=data)                                      
  return r.json()                                                             
# Использование                           
if __name__ == '__main__':                
#    TOKEN = 'your_bot_token_here'        
#   CHATID = 'your_chat_id_here'              
    IMAGE_TEXT = 'Hello, Telegram!'           
    IMAGE_FILENAME = 'Magic_Poser.jpg'                                                  
# Отправляем изображение                  
    result = send_photo(CHATID, IMAGE_FILENAME, TOKEN)                              
#    print(result)
