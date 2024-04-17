from flask import Flask, render_template, request, redirect

from datetime import datetime, timezone, timedelta

app = Flask(__name__, template_folder="templates")   

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/time")
def time_now_est():
    current_time = datetime.now()
    new_timezone = timezone(timedelta(hours=-5))  # Change this to the timezone you want

    # Convert the datetime object to the new timezone
    new_time = current_time.astimezone(new_timezone)
    current_time_str = new_time.strftime("%H:%M:%S")

    return f"Hello Aadil! The time is {current_time_str}"

@app.route("/date")
def date_today():
    current_date = datetime.now().date()
    return f"Hello Aadil! The date is {current_date}"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
 