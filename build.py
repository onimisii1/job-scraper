import json
import config
from scraper.sources import fetch_jobs
from scraper.filters import is_match

from datetime import datetime, timezone
import os


all_jobs = []

for company in config.COMPANIES:
    jobs = fetch_jobs(company)
    

    for job in jobs:
        all_jobs.append({
            "company": company,
            "title": job["title"].strip(),
            "location": job["location"]["name"].strip(),
            "url": job["absolute_url"],
        })
    print(f"{company}: {len(jobs)} jobs")

updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

output = {
    "updated":updated,
    "count":len(all_jobs),
    "jobs":all_jobs,
}

os.makedirs("docs", exist_ok=True)             
with open("docs/jobs.json", "w", encoding="utf-8") as f:
    json.dump(all_jobs, f, indent=2)             

print(f"Saved {len(all_jobs)} jobs to docs/jobs.json")


   

