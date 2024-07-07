import json
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

@app.route("/add-user", methods=["GET", "POST"])
def add_user():
    
    if request.method == "POST":
        username = request.json.get("username")
        age = request.json.get("age")
        husband_name = request.json.get("husband_name")
        
        full_name = f"{username} and {husband_name} is {age} years old"
        
        return jsonify({"message": full_name})
    else:
        return render_template('index.html')
    
@app.route("/")
def index():
    return render_template('index-abc.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/services")
def services():
    return render_template('services.html')