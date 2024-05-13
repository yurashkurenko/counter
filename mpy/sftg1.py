boundary="--97d81ac404017fec19458e34bae65b01--"
crlf = "\\r\\n\\r\\n"
chatpart="Content-Disposition: form-data; name="chat_id"\r\n\r\n159085018\r\n"
imagepart="Disposition: form-data; name=\"photo\"; filename=\"Magic_Poser.jpg"
def multupartdata(chatid,image):
    mpdata=boundary+crlf+chatpart+imagepart
    print(mpdata)
    return mpdata
     
multupartdata("12345","image")
