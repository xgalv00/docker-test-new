from flask import Flask
import threading
import time
import logging

app = Flask(__name__)


@app.before_first_request
def activate_job():
    def run_job():
        while True:
            logging.warning("Run recurring task")
            time.sleep(0.25)

    thread = threading.Thread(target=run_job)
    thread.start()


@app.route('/')
def index():
    return '<body>Hello world from DOCKER B. <a href="/about/">About this page</a>.</body>'


@app.route('/about')
def about():
    return '<body>This is the about page</body>'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
