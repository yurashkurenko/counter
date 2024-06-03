from settings import url,deviceid
from getpara import getpara
para=getpara(url,deviceid)
CAPTION=para['description']
IMAGE_FILENAME='girl.jpg'
from settings import TOKEN,CHATID
print(TOKEN)
print(CHATID)
print(IMAGE_FILENAME)
print(CAPTION)
CAPTION='Идентификатор устройства: '+deviceid+'\r\n'+CAPTION
#TOKEN, CHATID, IMAGE_FILENAME, CAPTION
import sendtg7
sendtg7.send_photo(TOKEN, CHATID, IMAGE_FILENAME, CAPTION)
