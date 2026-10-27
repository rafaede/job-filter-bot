import requests
import json

response = requests.get("https://remotive.com/api/remote-jobs?category=software-dev")
print(response.status_code)

job = response.json()
with open("remotive_cache.json", "w") as f:
    json.dump(job, f)

print(len(job["jobs"]))

for jobs in job["jobs"][:10]:
    if jobs['candidate_required_location'] == "Worldwide":
        if "Senior" not in jobs['title'] and "Lead" not in jobs['title'] and "Sr" not in jobs['title']:
            print(f"Title : {jobs['title']}, Company Name : {jobs['company_name']}")