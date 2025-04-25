from flask import Flask, render_template, request, jsonify
import subprocess
import os
import sys

app = Flask(__name__)

CODE_FILE = "voice_code_temp.py"

def run_code(code):
    with open(CODE_FILE, "w") as f:
        f.write(code)
    try:
        output = subprocess.check_output([sys.executable, CODE_FILE], stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return e.output

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run():
    data = request.get_json()
    code = data.get("code", "")
    output = run_code(code)
    return jsonify({"output": output})

if __name__ == "__main__":
    app.run(debug=True)
