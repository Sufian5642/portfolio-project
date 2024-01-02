from flask import Flask,render_template,send_from_directory
import os
app=Flask("__name__")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/morse')
def morse():
    return render_template("Morse code.html")
@app.route('/brick')
def brick():
    return render_template("Arcade.html")
@app.route('/typing')
def typing():
    return render_template("Typing Speed Checker.html")
@app.route('/Tic')
def Tic():
    return render_template("portfolio-details.html")
@app.route("/index/certificate")
def certificate():
    return send_from_directory('static', 'Python Developer Bootcamp.pdf')
@app.route("/research")
def research():
    return send_from_directory('static', 'OWC.pdf')
@app.route("/finalyearproject")
def finalyearproject():
    return send_from_directory('static', 'BCW.pdf')

if __name__=="__main__":
    app.run(debug=True)