import config
from scraper.sources import fetch_jobs
from scraper.filters import is_match
from scraper.storage import save_csv

matches = []

for company in config.COMPANIES:
    # your loop from lesson 5, but:
    #   is_match(title, config.INCLUDE, config.EXCLUDE)

    save_csv(matches, config.OUTPUT_FILE)
print(f"Saved {len(matches)} jobs to {config.OUTPUT_FILE}")