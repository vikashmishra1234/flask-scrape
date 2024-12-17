from flask import Flask, jsonify, request
from Scraper import Scraper
import os
app = Flask(__name__)

# Define a basic route
@app.route('/')
def home():
    return "Welcome to Flask!"

# Define a route with a parameter
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

# Define a route that accepts GET and POST methods
@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'GET':
        url = request.args.get('url')
        data = Scraper(url)
        # data = Scraper(url) 
        return jsonify({"received": data}), 201
    else:  # GET request
        return jsonify({"message": "Send a POST request with some data"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render's port or fallback to 5000
    app.run(host="0.0.0.0", port=port)
