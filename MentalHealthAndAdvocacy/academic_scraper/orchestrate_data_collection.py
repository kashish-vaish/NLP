import subprocess

def run_script(script_path):
    print(f"\nRunning {script_path}...")
    result = subprocess.run(["python", script_path], capture_output=True, text=True)
    print(result.stdout)
    print(result.stdout)
    if result.stderr:
        print(f"Errors in {script_path}:")
        print(result.stderr)
    print(f"Finished {script_path}.")

if __name__ == "__main__":
    print("Starting full data collection orchestration...\n")

    # Step 1: Scrape metadata
    run_script("main.py")

    # Step 2: Download PDFs
    run_script("download_pdfs.py")

    # Step 3: Extract full text from PDFs
    run_script("extract_texts.py")

    print("\nData collection phase complete! Ready for merging and EDA.")
