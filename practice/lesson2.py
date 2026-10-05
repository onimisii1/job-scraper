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

# Lesson 2 recap:

# A for loop runs the same lines once for every item in a list.
# Inside the loop, job is one dictionary, so everything about that job comes from job[...].
# if "word" in text: checks whether text contains a word; for doesn't check anything.
# Indentation controls when a line runs: once, for every job, or only for the jobs that match.
# count = count + 1 uses the same name on both sides to make it go up.