def multupartdata(chat_id,image):
    boundary="--97d81ac404017fec19458e34bae65b01--"
    crlf = "\\r\\n"
    crlf2 = "\\r\\n\\r\\n"
    chatpart="Content-Disposition: form-data; name='chat_id'"\r\n\r\n"+chat_id+"\r\n"
    #Content-Type: multipart/form-data
    filename="Magic_Poser.jpg"
    imagepart="Disposition: form-data; name='photo'; filename="+filename
    mpdata=boundary+crlf+chatpart+boundary+crlf+imagepart+crlf+boundary
    print(mpdata)
    return mpdata
    
def sendphotototg(token,chat_id,image):
    url="api.telegram.org"
    urltile="/bot1701291551:AAEk2TbH7mbHLPVVBrP0gEOSZBezbjH1FHY/sendPhoto HTTP/1.1\r\n"
    #User-Agent: python-requests/2.31.0\r\nAccept-Encoding: gzip, deflate\r\n
    #Content-Type: multipart/form-data; boundary=97d81ac404017fec19458e34bae65b01\r\n\r\n'
    header="Content-Type: multipart/form-data; boundary=97d81ac404017fec19458e34bae65b01\r\n\r\n"
    data=multupartdata(chat_id,image)
    print(url)
    print(url)
    print(header)
    return mpdata
          
multupartdata("159085018","image")
