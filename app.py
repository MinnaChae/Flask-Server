from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/minnachae')
def hello_world():
    return "Hello world from Minna"

@app.route('/datetime')
def get_datetime():
    now = datetime.datetime.now()
    return f"Today's date is {now.strftime('%Y-%m-%d')} and the current time is {now.strftime('%H:%M:%S')} UTC"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=5000)
