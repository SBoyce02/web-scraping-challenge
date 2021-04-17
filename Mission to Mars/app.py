from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/phone_app")


@app.route("/")
 def home():
    Mars_date = mongo.db.collection.find_one()
     return render_template("index.html", Mars = Mars_data)


@app.route("/scrape")
def scraper():
  
    Mars_data = scrape_mars.scrape_info()
    mongo.db.collection.update({}, Mars_data, upsert=Ture) 
   
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
