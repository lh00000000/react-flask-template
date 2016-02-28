import logging

from flask import Flask
from flask import render_template

logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
