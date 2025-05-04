# Evolution of Mental Health Language

## Overview
This project analyzes the evolution of mental health discourse across scientific (arXiv) and media (Guardian) sources from 1990–2023. It measures bias and sentiment trends and assesses the impact of advocacy efforts.

## Research Goals
- Detect bias (supportive, stigmatizing, neutral framing)
- Track sentiment (positive/negative tone)
- Correlate changes with real-world advocacy events

## Methods
- Data Collection: arXiv API, Guardian News API
- Sentiment Analysis: distilBERT model (Hugging Face)
- Bias Detection: BART-MNLI zero-shot classification
- Trend Analysis: Sentiment and bias over years

## Key Results
- Advocacy correlates with increased supportive framing.
- Media shows faster adaptation to advocacy than academia.

## Project Structure
- `academic_scraper/` – Scripts for scraping and extraction
- `EDA/` – Exploratory and advanced analysis notebooks
- `data/` – Raw and processed data
- `presentation/` – Slides and Poster

## Acknowledgments
- Hugging Face, ArXiv, Guardian APIs
- CS533 NLP Course

