import csv

def save_csv(matches, filename):
    with open("jobs.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["company", "title", "location", "url"])
        writer.writeheader()
        writer.writerows(matches)
