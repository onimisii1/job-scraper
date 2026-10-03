import requests
response = requests.get("https://boards-api.greenhouse.io/v1/boards/stripe/jobs")
data = response.json()
jobs = data["jobs"]

count = 0

for job in jobs:
    title = job["title"]
    location = job["location"]["name"]
    print(f"{title} | {location}")


    if "Engineer" in title:
        count = count + 1
print(count)
