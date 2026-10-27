import json

with open("remotive_cache.json", "r") as f:
    job = json.load(f)

print(len(job["jobs"]))

for jobs in job["jobs"][:10]:
    if jobs['candidate_required_location'] == "Worldwide":
        if "Senior" not in jobs['title'] and "Lead" not in jobs['title'] and "Sr" not in jobs['title']:
            print(f"Title : {jobs['title']}, Company Name : {jobs['company_name']}")