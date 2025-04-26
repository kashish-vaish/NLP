from semantic_scholar_scraper import fetch_from_semantic_scholar
from arxiv_scraper_multi import fetch_from_arxiv_multi
from utils import save_json, save_csv

# Parameters
SEMANTIC_QUERY = (
    "depression OR anxiety OR stress detection OR emotion recognition OR suicidal ideation "
    "OR mental disorder OR mental illness OR wellbeing OR social support OR therapy chatbot OR psychiatric diagnosis"
)

YEAR_START = 1990
YEAR_END = 2023
LIMIT = 200

ARXIV_KEYWORDS = [
    "depression", "anxiety", "stress detection", "emotion recognition",
    "suicidal ideation", "mental disorder", "mental illness", "wellbeing",
    "social support", "therapy chatbot", "psychiatric diagnosis"
]

# --- Fetch from Semantic Scholar ---
print("Fetching from Semantic Scholar...")
sem_data = fetch_from_semantic_scholar(SEMANTIC_QUERY, YEAR_START, YEAR_END, limit=LIMIT)

# --- Fetch from arXiv ---
print("\nFetching from arXiv (multiple keywords)...")
arxiv_data = fetch_from_arxiv_multi(ARXIV_KEYWORDS, YEAR_START, YEAR_END, max_results_per_keyword=300)

# --- Save Metadata Only ---
print("\nSaving metadata results...")

# Semantic Scholar
save_json(sem_data, "../data/semantic_scholar_results.json")
save_csv(sem_data, "../data/semantic_scholar_results.csv")

# arXiv
save_json(arxiv_data, "../data/arxiv_multi_keywords_results.json")
save_csv(arxiv_data, "../data/arxiv_multi_keywords_results.csv")

print("\nMetadata collection complete! Ready for PDF download and extraction steps.")
