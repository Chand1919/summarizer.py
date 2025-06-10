from fpdf import FPDF
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

# 🔹 1. Generate summary PDF
def generate_summary_pdf(summary_text, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Split long lines for PDF readability
    for line in summary_text.split('\n'):
        pdf.multi_cell(0, 10, line)

    pdf.output(output_path)


# 🔹 2. Extract text from scanned PDF using OCR
def extract_text_from_scanned_pdf(pdf_path):
    pages = convert_from_path(pdf_path)
    text = ""
    for i, image in enumerate(pages):
        page_text = pytesseract.image_to_string(image, lang='eng')
        print(f"Page {i+1} OCR Text:\n", page_text)
        text += page_text + "\n"
    return text.strip()


