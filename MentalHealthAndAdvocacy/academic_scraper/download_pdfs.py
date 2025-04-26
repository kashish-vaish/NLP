import os
import requests
import json

def safe_download_pdf(pdf_url, save_dir="../data/pdf", timeout=20, min_size_kb=20):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    filename = os.path.join(save_dir, pdf_url.split('/')[-1] + ".pdf")

    try:
        with requests.get(pdf_url, stream=True, timeout=timeout) as r:
            size_kb = int(r.headers.get('Content-Length', 0)) / 1024
            if r.status_code != 200 or size_kb < min_size_kb:
                print(f"Skipping (too small or invalid) {pdf_url}")
                return None

            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        print(f"Downloaded: {filename}")
        return filename

    except Exception as e:
        print(f"Failed to download {pdf_url}: {e}")
        return None

def batch_download_from_json(json_path):
    """
    Load arXiv JSON results and download all PDFs safely.
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        papers = json.load(f)

    success_count = 0
    fail_count = 0

    for paper in papers:
        pdf_url = paper.get('pdf_url')
        if pdf_url:
            result = safe_download_pdf(pdf_url)
            if result:
                paper['local_pdf_path'] = result
                success_count += 1
            else:
                paper['local_pdf_path'] = None
                fail_count += 1

    # Save updated metadata
    updated_path = json_path.replace('.json', '_with_pdf_paths.json')
    with open(updated_path, 'w', encoding='utf-8') as f:
        json.dump(papers, f, indent=2, ensure_ascii=False)

    print(f"\nDownload complete. Success: {success_count}, Failures: {fail_count}")
    print(f"Updated metadata saved to: {updated_path}")

if __name__ == "__main__":
    batch_download_from_json("../data/arxiv_multi_keywords_results.json")