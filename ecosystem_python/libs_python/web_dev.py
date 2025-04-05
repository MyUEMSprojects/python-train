# flask (Micro-framework)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

# django (Full-stack framework)
django-admin startproject mysite


