def multupartdata(chat_id,image):
    boundary="--97d81ac404017fec19458e34bae65b01--"
    crlf = "\\r\\n\\r\\n"
    chatpart="Content-Disposition: form-data; name="+chat_id+"\r\n\r\n159085018\r\n"
    filename="Magic_Poser.jpg"
    imagepart="Disposition: form-data; name="+photo+"; filename="+filename
    mpdata=boundary+crlf+chatpart+boundary+crlf+imagepart+crlf+boundary
    print(mpdata)
    return mpdata
     
multupartdata("12345","image")
