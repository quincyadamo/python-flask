
from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "secretKey"
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/result', methods=['POST'])
def submit_info():
   name = request.form['name']
   location = request.form['location']
   language = request.form['language']
   if len(request.form['name']) < 1:
		flash("Please type your name!")
   elif len(request.form['location']) < 1:
		flash("Tell us where you're from!")
   elif len(request.form['language']) < 1:
        flash("How will we communicate without knowing your language of choice!")
   else:
        flash("Success!")
        return render_template("result.html", name=name, location=location, language=language)

   return redirect('/')

app.run(debug=True) # run our server
