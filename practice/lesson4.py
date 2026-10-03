import requests



def fetch_jobs(company):
    url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"
    response = requests.get(url)
    data = response.json()
    return data["jobs"]
jobs = fetch_jobs("stripe")
print (len(jobs))

def is_match(title):
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