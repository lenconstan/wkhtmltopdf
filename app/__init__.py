from flask import Flask, render_template, url_for, request
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)



from app import routes