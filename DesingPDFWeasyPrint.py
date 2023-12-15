from weasyprint import HTML

def create_pdf_from_html(html_file, pdf_file):
    HTML(html_file).write_pdf(pdf_file)


with open("PDFfile.html","w") as file:
    file.write("<b> Information of patient </b>")


html_file_name = '/Users/atitsharma/Desktop/Atit destop/Learning python/PDFfile.html'
pdf_file_name = 'styled_pdf.pdf'


create_pdf_from_html(html_file_name, pdf_file_name)

