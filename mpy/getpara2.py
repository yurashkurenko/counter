import urequests as requests

def getpara(url,dev):
    data = { 'device_id': dev }
    headers = { 'Content-Type': 'application/json' }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        print("Response from server:", response.json())
        getpara=response.json()
    else:
        print("Failed to get device parameters. Status code:", response.status_code)
        getpara={"status":"None"}
