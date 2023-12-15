from reportlab.pdfgen import canvas

def create_pdf(file_name):
    # Create a PDF document
    pdf = canvas.Canvas(file_name)

    # Add text to the PDF
    pdf.drawString(100, 750, "<h1>Hello, this is a PDF created with Python! <h1>")

    # Save the PDF
    pdf.save()

# Provide a file name for your PDF
pdf_file_name = "example.pdf"

# Create the PDF
create_pdf(pdf_file_name)
