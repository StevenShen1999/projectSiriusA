from flask_restplus import Api
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Configuration

# Flask
app = Flask(__name__)
api = Api(app, version="0.0.1", title="SiriusA",
description="Steven Shen's personal website")

# Congiguration
app.config.from_object(Configuration)

# SQLAlchemy
db = SQLAlchemy(app)

# Flask-restplus
from namespaces.blog import api as blog

api.add_namespace(blog, path="/blog")

# CORS
CORS(app)