import config
from scraper.sources import fetch_jobs
from scraper.filters import is_match

from flask import Flask

app = Flask(__name__) #creates the webapp

@app.route("/") # when someone visits the ("/") home page

def home():
    return "Welcome to my web Job Scraper" # return this text


@app.route("/count") #so,oen visits the count page
def count():
    total = 0
    for company in config.COMPANIES:
        jobs =  fetch_jobs(company)
        
        for job in jobs:
            title = job["title"].strip()
            if is_match(title, config.INCLUDE, config.EXCLUDE):     # ← change 1
                total = total + 1
                
    return f"Found {total} matching jobs"
if __name__ == "__main__":
    app.run(debug=True) #atart the app

