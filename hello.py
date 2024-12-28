from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'It's Lunch Time as always!!!'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)
