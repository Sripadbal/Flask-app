from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('site.html')

@app.route('/mysite2.html')
def about():
    return render_template('mysite2.html')  

