from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/home')
def hello():
    d="anjaly"
    return render_template('home.html',n=d)

@app.route('/index')
def index():
    x=[1,2,3,4,5]
    y={'name':'Anjaly','Age':'21'}
    return render_template('home2.html',n=x,s=y)


if __name__ =='__main__':
    app.run(debug=True,port=8011)