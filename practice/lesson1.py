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

# What Lesson 1 taught you:

# requests.get() downloads a URL, and .json() (with the brackets) turns the result into Python data.
# API data is nested: dictionaries inside lists inside dictionaries. Go one level at a time, with one [ ] per level.
# When you're unsure what something is, check with print(type(x)) and print(x.keys()) before using it.
# KeyError means you looked up a key that dictionary doesn't have, which usually means you're at the wrong level.