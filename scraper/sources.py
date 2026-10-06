import requests

def fetch_jobs(company):
    url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"
    try:
        response = requests.get(url, timeout=20)
    except requests.RequestException as error:
        print(f" ! {company} could not connect ({error})")
        return[]
    if response.status_code != 200:      # != means "not equal to"
        print(f"  ! {company}: got status {response.status_code}, skipping")
        return []                        # hand back an empty list instead of crashing

    data = response.json() #converting it to JSON
    return data["jobs"]
