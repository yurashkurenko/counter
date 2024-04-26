import netphone
import requests
url = "https://raw.githubusercontent.com/yurashkurenko/counter/main/hello.py"
r=requests.get(url)
print(r.text)
with open("myprog.py", "w") as f:
    # Write the text data to the file
    f.write(r.text)
import myprog