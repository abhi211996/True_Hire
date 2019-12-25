#import mysql.connector

import MySQLdb
from flask import Flask,render_template,request,url_for,redirect

app=Flask(__name__)
@app.route("/")
#@app.route("/RegForm.html")
def hello():
    return render_template('test.html')





@app.route('/mov')
def mov():
    db = MySQLdb.connect(user='root', password='', host='localhost', database='Student')
    ob = db.cursor()
    # zero=0;
    query= "select Email from registration;"
    result = ob.execute(query)

    data =ob.fetchall()
    return render_template('student1.html',m=data)
    db.commit()
    db.close()



if __name__ == "__main__":
    app.run(debug=True)