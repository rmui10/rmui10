#Team Asinine - Winnie Huang, Renee Mui, Anya Zorin
#SoftDev
#K10 -- Putting Little Pieces Together: look through flask starter kit
#2020-10-11

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
#if the '/' is changed, the url where the text is displayed also changes
def hello_world():
    return "No hablo queso!" #displays "No hablo queso! on the webpage

app.run()

#in order to see changes, you have to restart the server

