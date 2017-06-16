from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world. <a href="/about">About this page</a>.'

@app.route('/about')
def about():
    return 'This is the about page'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
