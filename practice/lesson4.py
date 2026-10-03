import requests



def fetch_jobs(company):
    url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"
    response = requests.get(url)
    data = response.json()
    return data["jobs"]
jobs = fetch_jobs("stripe")
print (len(jobs))