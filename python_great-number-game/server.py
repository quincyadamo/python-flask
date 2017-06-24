from flask import Flask , render_template, request, redirect, session, flash
import random

app=Flask(__name__)
app.secret_key='secret'

@app.route('/')
def index():

    if 'didWin' not in session:
        session["didWin"]='neutral'
    if 'message' not in session:
        session["message"]=""
    if 'number' not in session:
        session['number']=random.randrange(1,101)
    return render_template("index.html", didWin=session['didWin'], message=session['message'] )

@app.route('/guess', methods=['POST'])
def guess():
    guess=int(request.form['number'])
    print guess
    if guess == session['number']:
        session['message']= "Winner! The number was " + str(session['number'])
        session['didWin'] = 'yes'
        return redirect('/')
    if guess > session['number']:
        session['message']= 'Too High!'
    elif guess < session['number']:
        session['message']= 'Too Low!'

    session['didWin'] = 'no'
    return redirect('/')


@app.route('/reset')
def reset():
    session.pop("didWin")
    session.pop("number")
    session.pop("message")
    return redirect('/')

app.run(debug=True) ## MOST IMPORTATANT
