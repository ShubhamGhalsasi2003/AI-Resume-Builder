import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    # Open the provided PDF file
    document = fitz.open(pdf_path)
    
    full_text = ""
    
    # Iterate through all the pages in the PDF
    for page_num in range(len(document)):
        page = document.load_page(page_num)  # Get the page
        full_text += page.get_text("text")  # Extract text from the page
    
    return full_text

# Test the function with a sample PDF
pdf_path = "path/to/your/resume.pdf"
text = extract_text_from_pdf(pdf_path)

# Print extracted text
print(text)
