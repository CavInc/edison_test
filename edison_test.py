import uuid

from flask import Flask,json,render_template
from flask import request,session

from api import pages

app = Flask(__name__)

BASE_DIR = app.root_path

app.secret_key = '\xb6%\x80\xcd\xfb\x8a\r\xd3\x01q\xcb\xd9\xe1\x12\xcd}[\xafM\xe5\xad\r\x03\x81'

@app.route('/')
def index():
    print session
    print request
    print request.cookies
    if 'username' in session:
        print "YES"
        print session.viewkeys()
    else :
        print "NO"
        name = str(uuid.uuid4())
        session['username'] = name
    return pages.index(session['username'])

@app.route('/api/get_extrasense_value',methods=['POST'])
def getExtrasenseValue():
    return pages.getExtrasenseAnswer(session['username'])

@app.route('/api/user_value',methods=['POST'])
def setUserValue():
    return pages.setUserNumber(request,session['username'])

@app.route('/api/user_history',methods=['POST'])
def getUserHistory():
    res = pages.getUserHistory(session['username'])
    return render_template("table_user_his.html",userHis = res)
    #return json.dumps(res)

@app.route('/api/extrasense_raiting',methods=['POST'])
def getExtrasenseRaiting():
    return pages.getExtrasenseRaiting()

@app.route('/api/extrasense_history',methods=['POST'])
def getExtrasenseHistory():
    res = pages.getExtrasenseHistory(session['username'])
    return render_template("table_extra_his.html",expHistory = res)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
