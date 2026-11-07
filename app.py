
import os
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "shopsmart_model.pkcls")

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html")
