from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import credentials

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = credentials.username
app.config['MYSQL_PASSWORD'] = credentials.password #last 4 of onid
app.config['MYSQL_DB'] = credentials.username
app.config['MYSQL_CURSORCLASS'] = "DictCursor"


mysql = MySQL(app)


# Routes
@app.route('/')
def root():
    query = "SELECT * FROM diagnostic;"
    query1 = 'DROP TABLE IF EXISTS diagnostic;';
    query2 = 'CREATE TABLE diagnostic(id INT PRIMARY KEY AUTO_INCREMENT, text VARCHAR(255) NOT NULL);';
    query3 = 'INSERT INTO diagnostic (text) VALUES ("MySQL is working!")';
    query4 = 'SELECT * FROM diagnostic;';
    cur = mysql.connection.cursor()
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    cur.execute(query4)
    results = cur.fetchall()

    return "<h1>MySQL Results</h1>" + str(results[0])


# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted
    app.run(port=80320, debug=True)