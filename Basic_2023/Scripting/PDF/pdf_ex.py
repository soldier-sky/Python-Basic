"""
Example program to perform pdf operation using python library.
"""

import PyPDF2

# below routine opens dummy pdf and read the page -> rotate the page and write to new pdf file
with open('dummy.pdf', 'rb') as fin:
    reader = PyPDF2.PdfReader(fin)
    print(len(reader.pages))  #prints total no. of pages in pdf
    page = reader.pages[0]
    rotated_page = page.rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(rotated_page)
    with open('rotated_dummy.pdf', 'wb') as fout:
        writer.write(fout)



# template = PyPDF2.PdfReader(open('super.pdf', 'rb'))
# watermark = PyPDF2.PdfReader(open('watermark.pdf', 'rb'))
# output = PyPDF2.PdfWriter()
 
# for i in range(len(template.pages)):
#     page = template.pages[i]
#     page.merge_page(watermark.pages[0])
#     output.add_page(page)
 
#     with open('watermarked.pdf', 'wb') as file:
#         output.write(file)