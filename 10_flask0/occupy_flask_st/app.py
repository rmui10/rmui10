#Team Asinine - Winnie Huang, Renee Mui, Anya Zorin
#SoftDev
#K10 -- Putting Little Pieces Together: display random job on webpage
#2020-10-11

from flask import Flask
import occupations #imports occupation file so we can use its methods

app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def printAll(): #prints roster and jobs
    return printRoster() + occupations.getJob() + '</br>' + printJobs()

@app.route("/") 
def printJobs():
    jobs = list(occupations.getDict()['job occupation']) #makes list of occupations
    return '</br> OCCUPATIONS </br>' + '</br>'.join(jobs) #return occupations separated by new line
    
def printRoster(): #prints roster and team name
    return 'Team Asinine - Winnie Huang, Renee Mui, Anya Zorin </br></br>'

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

