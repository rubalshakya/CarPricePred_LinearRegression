from flask import Flask,render_template,request
from project_app.utils import CarPricePrediction

app = Flask(__name__)

@app.route("/")
def base():
    return render_template("home.html")


@app.route("/predict",methods = ["POST","GET"])
def home():
    if request.method=="POST":
        data = dict(request.form)
        CarPrice = CarPricePrediction(data)
        price = CarPrice.get_PredCarPrice()
        return render_template("after.html",result = price)

if __name__ == "__main__":
    app.run(debug=True)