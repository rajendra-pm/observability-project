from flask import Flask, request
import logging
import random
import time

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def home():
    logging.info("Home endpoint hit")
    return "Hello Observability!"

@app.route('/process')
def process():
    logging.info("Process endpoint hit")
    time.sleep(random.randint(1,3))
    return "Processed"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
