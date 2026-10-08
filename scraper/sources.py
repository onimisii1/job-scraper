import requests

def fetch_jobs(company):
    url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

    for attempt in range(3):                     # try up to 3 times
        try:
            response = requests.get(url, timeout=60)
            break                                # success: leave the retry loop
        except requests.RequestException as error:
            print(f"  ! {company}: attempt {attempt + 1} failed ({error})")
    else:
        return []                                # all 3 attempts failed

    if response.status_code != 200:
        print(f"  ! {company}: got status {response.status_code}, skipping")
        return []

    data = response.json()
    return data["jobs"]