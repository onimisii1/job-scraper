import requests
response = requests.get("https://boards-api.greenhouse.io/v1/boards/stripe/jobs")
print(response.status_code) #200 means good
data = response.json()
print(data.keys())        # shows which keys a dictionary has
print(type(data["jobs"])) # is this a list? a dict? a string?
jobs = data["jobs"]
number_of_jobs = len(jobs)
print(number_of_jobs)
print(type(jobs))
first_job = jobs[0]
print(first_job["title"])