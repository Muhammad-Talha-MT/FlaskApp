import logging
import time
from flask import Flask



request_count = 0
app = Flask(__name__)

@app.route("/")
def hello():
    global request_count
    request_count += 1
    count = request_count
    logging.debug(str(count) + ': Hello - Begin')
    time.sleep(2)
    logging.debug(str(count) + ': Hello - End')
    return "<h1 style='color:blue'>Hello There!</h1>"

