import requests
import time

API_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

def fetch_from_semantic_scholar(query, year_start, year_end, limit=500):
    headers = {
        "User-Agent": "MentalHealthResearchBot/1.0"
    }

    results = []
    offset = 0
    batch_size = 100  # Max allowed by API

    while len(results) < limit:
        params = {
            "query": query,
            "offset": offset,
            "limit": batch_size,
            "fields": "title,abstract,authors,year,url,isOpenAccess"
        }

        response = requests.get(API_URL, headers=headers, params=params)

        if response.status_code != 200:
            print(f"Error: {response.status_code}, {response.text}")
            break

        data = response.json().get("data", [])
        filtered = [r for r in data if r.get("year") and year_start <= r["year"] <= year_end]
        results.extend(filtered)

        if len(data) < batch_size:
            break  # No more results

        offset += batch_size
        time.sleep(1)  # Respect API limits

    print(f"\nTotal Semantic Scholar papers fetched: {len(results)}")
    return results
