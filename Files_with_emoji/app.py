import base64
from cgi import print_environ
from email import message


with open("file_one") as file:
    data = file.read()
    lines = data.split("\n")
    message = lines [-1]  #Line with strange symbol
    print(message)
    

with open ("file_two") as file:
    data = file.read()
    lines = data.split("\n")
    message = lines[-1]
    print(message)
    
    
    message = message.encode()
    message = base64.b64encode(message)
    message = base64.b64decode(message).decode()

import emoji
print(emoji.emojize('Python is :thumbs_up:'))
client.send_message(chat, emoji.emojize(':wink:'))


import pandas as pd
data = pd.read_csv("Item tsv - Sheet1.tsv", sep="\t")

for note in data["note"]:
    print(note)