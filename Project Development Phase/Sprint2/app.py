from flask import Flask, render_template, redirect, request, url_for, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/enterdetail')
def enterdetail():
    return render_template('enterdetail.html')
@app.route('/detailconfirm')
def detailconfirm():
    return render_template('detailconfirm.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)