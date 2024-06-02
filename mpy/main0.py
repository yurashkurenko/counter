from settings import url,deviceid
from getpara import getpara
para=getpara(url,deviceid)
print(para)
from settings import url,deviceid
from getpara import getpara
para=getpara(url,deviceid)
CAPTION=para['description']
IMAGE_FILENAME='girl.jpg'
#TOKEN, CHATID, IMAGE_FILENAME, CAPTION
print(CAPTION)
import sendtg6
sendtg6.send_photo(TOKEN, CHATID, IMAGE_FILENAME, CAPTION)