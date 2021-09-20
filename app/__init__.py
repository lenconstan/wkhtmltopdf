from flask import Flask, render_template, url_for, request
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=False)

from app import routes