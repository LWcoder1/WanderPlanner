import os, requests, random, math, time
from flask import Flask, render_template, url_for, request
from apiTest import travelPlan, parseObjectToString
from locationAPI import returnCoordinates

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about_us')
def about_us():
    return render_template("about_us.html")


@app.route('/recommendations')
def recommendations():
    return render_template("recommendations.html")

@app.route('/itinerary')
def itinerary():
    return render_template("itinerary.html")


@app.route('/planner', methods=['GET', 'POST'])
def planner():
    if request.method == 'POST':
        location = request.form['location']
        ll = returnCoordinates(location)
        radius = int(request.form['radius'])
        days = int(request.form['totalDays'])
        travelPlans = travelPlan(ll, radius, days)
        travelPlans.dataPopulate()
        totalDays = []
        for day in range(days):
            totalDays.append(day)
        # we need for loop to solve this
        return render_template("itinerary.html",
                            duration=totalDays,
                            breakfastList=parseObjectToString(travelPlans.breakfastList[0]),
                            lunchList=parseObjectToString(travelPlans.lunchList[0]),
                            dinnerList=parseObjectToString(travelPlans.dinnerList[0]),
                            activityOneList=parseObjectToString(travelPlans.attractionList[0]),
                            activityTwoList=parseObjectToString(travelPlans.attractionList[1]),
                            activityThreeList=parseObjectToString(travelPlans.attractionList[2]),
                            )
    else:
        return render_template("planner.html")
    


if __name__ == "__main__":
    app.run(debug=True)
