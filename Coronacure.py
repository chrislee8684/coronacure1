from flask import Flask, render_template
import csv

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    counter=0
    with open('/home/chrislee8684/mysite/templates/Database.csv', 'r') as csv_file:  # opened csv to read only
        csv_reader = csv.reader(csv_file)  # returns csv as strings

        vaccinename = [] #list to save for loop iterations
        developer = []
        phase = []
        expect = []

        for line in csv_reader:  # each row in database
            vaccinename.append(line[0])
            developer.append(line[1])
            phase.append(line[2])
            expect.append(line[3])
            counter+=1 #row count

    return render_template('home.html', vaccinename=vaccinename, developer=developer, phase=phase, expect=expect, counter=int(counter)) #what varaible in html = what variable in python


@app.route('/recentnews')
def recentnews():
    return render_template('recentnews.html')

@app.route('/howtohelp')
def howtohelp():
    return render_template('howtohelp.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()