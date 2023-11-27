''' Example program to add water mark in pdf file'''
import PyPDF2

template = PyPDF2.PdfReader(open('merged_pdf.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('watermark.pdf', 'rb'))
output = PyPDF2.PdfWriter()
 
for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])    # watermark.pdf contain watermark which needed to be superimposed
    output.add_page(page)
 
    with open('watermarked.pdf', 'wb') as file:
        output.write(file)