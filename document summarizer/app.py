from flask import Flask, render_template, request, send_file
from file_parser import parse_file
from summarizer import summarize_text
from pdf_generator import generate_summary_pdf
import os
import pytesseract

# Set tesseract executable path (change if your installation path is different)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        try:
            raw_text = parse_file(filepath)
            summary = summarize_text(raw_text)
            output_path = os.path.join(OUTPUT_FOLDER, 'summary.pdf')
            generate_summary_pdf(summary, output_path)
            return send_file(output_path, as_attachment=True)
        except Exception as e:
            return f"Error processing file: {str(e)}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


