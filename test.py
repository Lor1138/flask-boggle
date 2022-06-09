from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

#configurate so debug toolbar doesn't intercept test files
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

