
from flask import Flask, render_template, request
from mbta_helper import find_stop_near

app = Flask(__name__)




@app.route('/', methods=["GET", "POST"])
def nearestStation():
    if request.method == "POST":
        placeName= request.form['placeName']
        nearestStation, isAccessible = find_stop_near(placeName)
        isAccessible = " " if isAccessible==1 else "not"
        return render_template("result.html", placeName = placeName, nearestStation = nearestStation, isAccessible = isAccessible)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
