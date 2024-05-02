#import netphone
import urequests
url = "https://raw.githubusercontent.com/yurashkurenko/counter/main/paraprog.py"
r=urequests.get(url)
print(r.text)
with open("paraprog.py", "w") as f:
    # Write the text data to the file
    f.write(r.text)
#import myprog
