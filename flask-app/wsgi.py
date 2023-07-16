import sys
import logging
from flask import Flask

# Activate the virtual environment if necessary
activate_this = '/path/to/virtual/environment/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/threzcmp/d4mn.life/flask-app')

app = Flask(__name__)

# Import your Flask app from app.py
from app import app as application

# source /home/threzcmp/virtualenv/d4mn.life/flask-app/3.9/bin/activate && cd /home/threzcmp/d4mn.life/flask-app