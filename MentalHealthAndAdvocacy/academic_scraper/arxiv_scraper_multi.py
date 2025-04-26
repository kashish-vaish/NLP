import feedparser
import time
import urllib

def fetch_from_arxiv_multi(keywords, year_start, year_end, max_results_per_keyword=500):
    """
    Fetch papers from arXiv for multiple keywords.

    Args:
        keywords (list): List of search keywords.
        year_start (int): Start year for filtering.
        year_end (int): End year for filtering.
        max_results_per_keyword (int): Max results to fetch for each keyword.

    Returns:
        list: Combined list of matching papers.
    """
    base_url = "http://export.arxiv.org/api/query?"
    all_results = []

    for keyword in keywords:
        print(f"\nSearching for keyword: {keyword}")
        encoded_keyword = urllib.parse.quote_plus(keyword)
        for start in range(0, max_results_per_keyword, 100):
            query_url = (
                f"{base_url}search_query=all:{encoded_keyword}&start={start}&max_results=100"
            )
            print(f"Fetching: {query_url}")
            feed = feedparser.parse(query_url)

            for entry in feed.entries:
                year = int(entry.published.split('-')[0])
                if year_start <= year <= year_end:
                    all_results.append({
                        "keyword": keyword,
                        "title": entry.title,
                        "authors": [a.name for a in entry.authors],
                        "abstract": entry.summary,
                        "year": year,
                        "url": entry.id,
                        "pdf_url": next((l.href for l in entry.links if l.type == "application/pdf"), None)
                    })

            time.sleep(3)
            if len(feed.entries) < 100:
                break

    print(f"\nTotal papers fetched: {len(all_results)}")
    return all_results

# Example usage:
if __name__ == "__main__":
    keywords = [
        "depression", "anxiety", "stress detection", "emotion recognition",
        "suicidal ideation", "mental disorder", "mental illness", "wellbeing",
        "social support", "therapy chatbot", "psychiatric diagnosis"
    ]
    results = fetch_from_arxiv_multi(
        keywords,
        year_start=1990,
        year_end=2023,
        max_results_per_keyword=300 
    )

    # Save to JSON
    import json
    with open("arxiv_multi_keywords_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("\nSaved results to arxiv_multi_keywords_results.json")
