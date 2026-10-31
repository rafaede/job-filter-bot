import json

def filter_remotive(jobs):
    hasil = []
    for job in jobs:
        if "Worldwide" in job['candidate_required_location'] and "Senior" not in job['title'] and "Lead" not in job['title'] and "Sr" not in job['title']:
            hasil.append(job)
            
    return hasil

with open("remotive_cache.json", "r") as f:
    job = json.load(f)

print(len(job["jobs"]))

hasil = filter_remotive(job["jobs"][:10])

for jobs in hasil:
    print(f"Title : {jobs['title']}, Company Name : {jobs['company_name']}")