def multupartdata(chat_id,image):
    boundary="--97d81ac404017fec19458e34bae65b01--"
    crlf = "\\r\\n\\r\\n"
    chatpart="Content-Disposition: form-data; name="+chat_id+"\r\n\r\n159085018\r\n"
    Content-Type: multipart/form-data
    filename="Magic_Poser.jpg"
    imagepart="Disposition: form-data; name="+photo+"; filename="+filename
    mpdata=boundary+crlf+chatpart+boundary+crlf+imagepart+crlf+boundary
    print(mpdata)
    return mpdata
    
def sendphotototg(token,chat_id,image):
    url="api.telegram.org"
    header="Content-Type: multipart/form-data"
    data=multupartdata(chat_id,image)
    print(url)
    print(url)
    print(header)
    return mpdata
          
multupartdata("12345","image")
