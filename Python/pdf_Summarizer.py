# pip install PyPDF2 transformers torch

import PyPDF2
from transformers import pipeline

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def summarize_text(text, max_length=150):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    pdf_path = input("Enter the PDF file path: ")
    text = extract_text_from_pdf(pdf_path)
    
    if text.strip():
        summary = summarize_text(text)
        print("\nSummary:\n", summary)
    else:
        print("No text found in the PDF.")
