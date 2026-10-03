import requests



def fetch_jobs(company): #a function to fetch the company
    url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"
    response = requests.get(url)
    data = response.json()
    return data["jobs"]
jobs = fetch_jobs("stripe")
print (len(jobs))

def is_match(title): # a function to exclude engineering jobs with manager and highschool in the title
    check = title.lower()
    return "engineer" in check and "manager" not in check and "high school" not in check

for company in ["stripe", "coinbase", "airbnb"]:
    jobs = fetch_jobs(company)
    count = 0
    for job in jobs:
        title = job["title"].strip()
        if is_match(title):
            count = count + 1
    print(f"{company}: {count} matching jobs")

#     Lesson 4 recap:

# def name(input): defines a function, and calling name(value) runs it.
# return hands back the result and ends the function, so it goes last.
# A function hides the details: fetch_jobs("coinbase") replaces five lines.
# Test each function on its own with inputs where you know the answer.
# When you restructure code, compare the results to the old version (143 = 143).