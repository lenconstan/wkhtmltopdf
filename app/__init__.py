from flask import Flask, render_template, url_for, request

app = Flask(__name__)

from app import routes