import urequests as requests

def getpara(url,dev):
    data = { 'device_id': dev }
    headers = { 'Content-Type': 'application/json' }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        getpara=response.json()
    else:
        getpara={"status":"None"}
    return getpara
