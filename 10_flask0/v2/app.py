#Team Asinine - Winnie Huang, Renee Mui, Anya Zorin
#SoftDev
#K10 -- Putting Little Pieces Together: look through flask starter kit
#2020-10-11

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...") #prints to the terminal
    print(__name__)   #where will this go? prints __main__ to the termainal
    return "No hablo queso!" #displayed on the webpage

app.run()

