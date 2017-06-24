from flask import Flask , render_template, request, redirect, session
from random import *

app=Flask(__name__)
app.secret_key='SecretKey'

@app.route('/')
def index():
    if randint(0,1) == 1:
        session['type'] = 'Ninja'
    else:
        session['type'] = 'Hacker'

    if 'count' not in session: # meaning they are new to the site
        session['count']=0

    session['count']+=1

    return render_template("index.html", sessionType=session['type'], count=session['count'])
@app.route('/addtwo')
def addtwo():
    session['count']+=1
    return redirect('/')

@app.route('/reset')
def reset():
    session['count']=0
    return redirect('/')


app.run(debug=True)
