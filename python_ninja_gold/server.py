import random
import datetime
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secreteKey"

@app.route('/')
def index():
    try:
        session['gold']
    except KeyError:
        session['gold'] = 0
    try:
        session['activities']
    except KeyError:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def money():
    if request.form['place'] == 'farm':
        this_gold = random.randrange(10, 21)
        session['gold'] += this_gold
        session['activities'].append(
            'Earned ' + str(this_gold) + ' gold pieces from the farm! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
        )
        return redirect('/')

    if request.form['place'] == 'cave':
        this_gold = random.randrange(5, 11)
        session['gold'] += this_gold
        session['activities'].append(
            'Earned ' + str(this_gold) + ' gold pieces from the cave! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
        )
        return redirect('/')

    if request.form['place'] == 'house':
        this_gold = random.randrange(2, 6)
        session['gold'] += this_gold
        session['activities'].append(
            'Earned ' + str(this_gold) + ' gold pieces from the house! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
        )
        return redirect('/')

    if request.form['place'] == 'casino':
        this_gold = random.randrange(-50, 51)
        if this_gold > 0:
            session['activities'].append(
                'Won ' + str(this_gold) + ' gold pieces from the casino! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
        elif this_gold < 0:
            if (this_gold * -1) > session['gold']:
                this_gold = session['gold'] * -1
            session['activities'].append(
                '<span class="red">Lost ' + str(this_gold * -1) + ' gold pieces at the casino...' +
                'Yikes! ({:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()) + '</span>'
            )
        elif this_gold == 0:
            session['activities'].append(
                "Went to the casino and broke even...can't be lucky " +
                'every time! ' +
                '({:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
        session['gold'] += this_gold
    return redirect('/')

app.run(debug=True)
