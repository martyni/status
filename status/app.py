from flask import Flask, request, send_from_directory, jsonify, render_template
import os
import json
app = Flask(__name__)
STATUS_FILE=os.path.expanduser("~/.status")

@app.route("/")
def get_status():
    with open(STATUS_FILE) as status:
       data = json.load(status)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
