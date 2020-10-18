"""
Team Sleep Deprived: Victoria Gao, Renee Mui, Anya Zorin
SoftDev
K13 -- Template for Success
2020-10-19
"""

from flask import Flask, render_template
import csv, random
app = Flask(__name__)

@app.route("/")
def hello():
    return "No hablo queso!"

@app.route("/occupyflaskst")
def get_job():
    with open("data/occupations.csv", "r", newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        header = next(csv_file) # get rid of the header
        dictionary = {} # initialize the dictionary
        for row in reader:
            dictionary[row[0]] = [float(row[1]),row[2]] # populate the dictionary
        del dictionary['Total'] #delete the last row
        percentages = [percent[0] for percent in dictionary.values()]
        random_job = random.choices(list(dictionary.keys()),weights = percentages, k=1)
        return render_template('tablified.html',
                           title = "K13 -- Template for Success",
                           jobs = list(dictionary.keys()),
                           percents = percentages,
                           urls = [url[1] for url in dictionary.values()],
                           r_job = random_job[0],
                           length = len(list(dictionary.keys()))
                           )

if __name__ == "__main__":
    app.debug = True
    app.run()

