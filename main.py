from flask import Flask, render_template, request
from opeartions import script, script2
import csv, time

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search", methods=['POST'])
def search():
    key = request.form["s"]

    try:
        if len(key) == 0:
            data = script.without_key()
            # print(data)
        else:
            data = script2.with_key(key)
            print(data)
        
        with open('files/resilt.csv', 'w', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(['product  Type', 'Category', 'Article Date', 'Article Title'])
            writer.writerows(data)

    except Exception as e:
        print(e)

    return render_template("result.html", searched_key=key, searched_data=data)

if __name__ == "__main__":
    app.run(debug=True)