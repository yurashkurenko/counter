import nw-one
import requests
#url = "https://raw.githubusercontent.com/yurashkurenko/counter/main/hello.py"
#progname="helloprog.py"
from paraprog import url, progname
r=requests.get(url)
print(r.text)
with open(progname, "w") as f:
    # Write the text data to the file
    f.write(r.text)
import progname
