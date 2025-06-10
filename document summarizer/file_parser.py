import os
import pandas as pd
import pdfplumber
from docx import Document
from pdf2image import convert_from_path
import pytesseract

# Tell Python where to find Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_scanned_pdf(pdf_path):
    pages = convert_from_path(pdf_path)
    text = ""
    for i, image in enumerate(pages):
        page_text = pytesseract.image_to_string(image, lang='eng')
        print(f"Page {i+1} OCR Text:\n", page_text)
        text += page_text + "\n"
    return text.strip()

def parse_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()

    if ext == '.pdf':
        all_text = ""
        with pdfplumber.open(filepath) as pdf:
            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                print(f"Page {i+1} Text:\n", page_text)
                if page_text:
                    all_text += page_text + "\n"

        if all_text.strip():
            return all_text.strip()
        else:
            print("No text found with pdfplumber. Using OCR...")
            return extract_text_from_scanned_pdf(filepath)

    elif ext in ['.csv', '.xlsx']:
        df = pd.read_excel(filepath) if ext == '.xlsx' else pd.read_csv(filepath)
        text_cols = df.select_dtypes(include=['object'])
        text = ''
        for col in text_cols.columns:
            text += ' '.join(text_cols[col].dropna().astype(str)) + ' '
        return text.strip()

    elif ext == '.docx':
        doc = Document(filepath)
        fullText = [para.text for para in doc.paragraphs]
        return '\n'.join(fullText).strip()

    elif ext == '.txt':
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read().strip()

    return "Unsupported file format."






