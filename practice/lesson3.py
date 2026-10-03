import requests
response = requests.get("https://boards-api.greenhouse.io/v1/boards/stripe/jobs")
data = response.json()
jobs = data["jobs"]

count = 0

for job in jobs:
    title = job["title"].strip()
    check = title.lower()
    


    if "engineer" in check and "manager" not in check and "high school" not in check:
        count = count + 1
print(count)
