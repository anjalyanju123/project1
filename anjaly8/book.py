from flask import Flask,request, send_from_directory
from flask import render_template
from werkzeug.utils import secure_filename
import os
import sqlite3 as sql
app = Flask(__name__)

BOOK_FOLDER = './BOOK_FOLDER'
app.config['BOOK FOLDER']=BOOK_FOLDER

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form',methods=['POST','GET'])
def form():
    if request.method== 'POST':
        nm=request.form['name']
        p=request.form['auhtor']
        f=request.files['files']
        filename=secure_filename(f.filename)
        f.save(os.path.join(app.config['BOOK_FOLDER'],filename))

        con=sql.connect("database.db")
        cur=con.cursor()
        cur.execute("INSERT INTO book(name.author,pdf) VALUES (?,?,?)",(nm,p,filename))
        con.commit()

        return render_template('result.html')
    return render_template('form.html')

if __name__ =='__main__':
    app.run()