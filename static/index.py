from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Damaylis2103'
app.config['MYSQL_DB'] = 'tickets'
mysql = MySQL()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/employees')
def about():
    return render_template('employees.html')

@app.route('/report')
def report():
    return render_template('report.html')

if __name__ =="__main__":
    app.run(debug=True)