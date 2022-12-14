import logging
from flaskapp import app

logging.basicConfig(level=logging.DEBUG, filename='flaskapp.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    app.run()
