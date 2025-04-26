import os
import json
from pdfminer.high_level import extract_text

def safe_extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return None

    try:
        text = extract_text(pdf_path)
        if len(text.strip()) < 100:
            print(f"Extracted text too short in {pdf_path}")
            return None
        return text.strip()

    except Exception as e:
        print(f"Failed to extract {pdf_path}: {e}")
        return None

def batch_extract_texts(json_with_paths):
    """
    Load updated JSON with local_pdf_path and extract text from available PDFs.
    """
    with open(json_with_paths, 'r', encoding='utf-8') as f:
        papers = json.load(f)

    extracted_records = []
    success_count = 0
    fail_count = 0

    for paper in papers:
        local_path = paper.get('local_pdf_path')
        if local_path:
            text = safe_extract_text_from_pdf(local_path)
            if text:
                paper['extracted_text'] = text
                extracted_records.append({
                    "title": paper.get("title"),
                    "year": paper.get("year"),
                    "url": paper.get("url"),
                    "source": "arxiv",
                    "extracted_text": text
                })
                success_count += 1
            else:
                paper['extracted_text'] = None
                fail_count += 1

    # Save all extracted data
    output_json = json_with_paths.replace('.json', '_extracted.json')
    output_csv = json_with_paths.replace('.json', '_extracted.csv')

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(extracted_records, f, indent=2, ensure_ascii=False)

    pd = None
    try:
        import pandas as pd
        df = pd.DataFrame(extracted_records)
        df.to_csv(output_csv, index=False)
    except ImportError:
        print("Pandas not installed. CSV export skipped.")

    print(f"\nExtraction complete. Success: {success_count}, Failures: {fail_count}")
    print(f"Saved extracted data to: {output_json}")
    print(f"(Optional CSV saved to: {output_csv})")

if __name__ == "__main__":
    batch_extract_texts("../data/arxiv_multi_keywords_results_with_pdf_paths.json")