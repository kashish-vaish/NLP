import pandas as pd
import json
import os

# Paths (adjust if needed)
SEMANTIC_PATH = "../data/semantic_scholar_results.csv"
ARXIV_PATH = "../data/arxiv_multi_keywords_results_with_pdf_paths_extracted.csv"
GUARDIAN_PATH = "../data/guardian_mental_health_articles.json"

OUTPUT_PATH = "../data/combined_master_dataset.csv"

def load_semantic_data(path):
    print(f"Loading Semantic Scholar data from {path}")
    df = pd.read_csv(path)
    df = df[['title', 'abstract', 'year', 'url']]
    df = df.rename(columns={'abstract': 'content'})
    df['source'] = 'semantic_scholar'
    return df

def load_arxiv_data(path):
    print(f"Loading arXiv extracted texts from {path}")
    df = pd.read_csv(path)
    df = df[['title', 'extracted_text', 'year', 'url']]
    df = df.rename(columns={'extracted_text': 'content'})
    df['source'] = 'arxiv'
    return df

def load_guardian_data(path):
    print(f"Loading Guardian news articles from {path}")
    with open(path, 'r', encoding='utf-8') as f:
        guardian_data = json.load(f)
    df = pd.DataFrame(guardian_data)
    df = df[['title', 'content', 'year', 'url']]
    df['source'] = 'guardian_news'
    return df

def merge_all():
    print("\nStarting merging process...")

    semantic_df = load_semantic_data(SEMANTIC_PATH)
    arxiv_df = load_arxiv_data(ARXIV_PATH)
    guardian_df = load_guardian_data(GUARDIAN_PATH)

    # Align columns
    all_data = pd.concat([semantic_df, arxiv_df, guardian_df], ignore_index=True)

    print(f"\nTotal combined records: {len(all_data)}")

    # Save
    all_data.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved combined master dataset to {OUTPUT_PATH}")

if __name__ == "__main__":
    merge_all()
