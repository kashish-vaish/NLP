from pdfminer.high_level import extract_text
import requests
import os

def download_and_extract_pdf(pdf_url, save_dir="./CS533_kv401/data/pdfs", timeout=20):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    filename = os.path.join(save_dir, pdf_url.split('/')[-1] + ".pdf")
    
    try:
        with requests.get(pdf_url, stream=True, timeout=timeout) as r:
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        text = extract_text(filename)
        return text
    except Exception as e:
        print(f"Failed to download or extract {pdf_url}: {e}")
        return None
