from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/biometricdetail')
def biometricdetail():
    return render_template('biometricdetail.html')
@app.route('/enterdetail')
def enterdetail():
    return render_template('enterdetail.html')
@app.route('/detailconfirm')
def detailconfirm():
    return render_template('detailconfirm.html')
@app.route('/searchfood')
def searchfood():
    return render_template('searchfood.html')
@app.route('/foodstatus')
def foodstatus():
    return render_template('foodstatus.html')
@app.route('/addcalorie')
def addcalorie():
    return render_template('addcalorie.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)