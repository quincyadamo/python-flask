from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = 'secretKey'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def ninja():
    flash('Its Megan Foxx')
    return render_template("/ninja.html", color = 'meganfoxx')

@app.route('/ninja/<color>', methods = ['GET'])
def ninja_color(color):
    if color == 'red':
        flash('Its Raphael!!!')
    elif color == 'blue':
        flash('Its Leonardo!!!')
    elif color == 'purple':
        flash('Its Donatello (my fav)!!!')
    elif color == 'orange':
        flash('Its Michelangelo!!!')
    else:
        return redirect('/ninja')

    return render_template("/ninja.html", color = color)

app.run(debug=True)
