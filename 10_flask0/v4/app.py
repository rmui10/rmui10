#Team Asinine - Winnie Huang, Renee Mui, Anya Zorin
#SoftDev
#K10 -- Putting Little Pieces Together: look through flask starter kit
#2020-10-11

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

#runs the same as the v3 as long as the file is not imported
