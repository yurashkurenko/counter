r=urequests.get(url)
print(r.text)
with open("paraprog.py", "w") as f:
    # Write the text data to the file
    f.write(r.text)
#import myprog
root@localhost:~/countbot/mp# cat paraprog.py
url = "https://raw.githubusercontent.com/yurashkurenko/counter/main/hello.py"
progname="helloprog.py"
