import pdfplumber

def extract_text_from_pdf(pdf_path):
    all_text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    all_text += page_text + "\n"
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return ""
    return all_text.strip()
