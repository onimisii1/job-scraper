import config
from scraper.sources import fetch_jobs
from scraper.filters import is_match
from scraper.storage import save_csv

matches = []

for company in config.COMPANIES:
    jobs = fetch_jobs(company)
    count = 0

    for job in jobs:
        title = job["title"].strip()
        location = job["location"]["name"].strip()
        if is_match(title, config.INCLUDE, config.EXCLUDE):     # ← change 1
            count = count + 1
            matches.append({
                "company": company,
                "title": title,
                "location": location,
                "url": job["absolute_url"],
            })

    print(f"{company}: {count} matching jobs")

save_csv(matches, config.OUTPUT_FILE)                            # ← change 2: no indent
print(f"Saved {len(matches)} jobs to {config.OUTPUT_FILE}")