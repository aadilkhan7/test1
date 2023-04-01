from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"Hello, World! The time is {current_time}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')