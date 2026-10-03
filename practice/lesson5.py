import requests
import csv

matches = []

def fetch_jobs(company): #a function to fetch the company
    url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"
    response = requests.get(url)
    data = response.json()
    return data["jobs"]


def is_match(title): # a function to exclude engineering jobs with manager and highschool in the title
    check = title.lower()
    return "engineer" in check and "manager" not in check and "high school" not in check

for company in ["stripe", "coinbase", "airbnb"]: # the final summary
    jobs = fetch_jobs(company)
    count = 0
    
    for job in jobs:
        title = job["title"].strip()
        location = job["location"]["name"].strip()
        if is_match(title):
            count = count + 1
            matches.append({
                "company": company,
                "title": title,
                "location": location,
                "url": job["absolute_url"],
            })
    print(f"{company}: {count} matching jobs")

with open("jobs.csv", "w", newline="", encoding="utf-8") as f: #to put it into the jobs.csv file, basically storing the information
    writer = csv.DictWriter(f, fieldnames=["company", "title", "location", "url"])
    writer.writeheader()
    writer.writerows(matches)
print(f"Saved {len(matches)} jobs to jobs.csv")

# Lesson 5 recap:

# Build a list of your own dictionaries with .append(), keeping only the fields you need.
# Where you create the list matters: before the loop, it builds up; inside the loop, it resets every time.
# Clean values into variables first, then use those variables.
# csv.DictWriter turns dictionaries into rows and handles commas and quotes for you.
# with open(...) closes the file safely, and a relative file name saves to wherever the terminal is.