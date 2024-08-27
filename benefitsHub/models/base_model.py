#!/usr/bin/python3
"""Module defines a base model for users and benefits"""
from flask import FLask

app = Flask(__name__)


class BaseUserModel:
    """class defines base user model"""
    id = db.Column(INTEGER)
