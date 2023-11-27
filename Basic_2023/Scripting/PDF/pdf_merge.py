'''Example program which merges input pdf file into single pdf file'''
import PyPDF2
import sys

inputs = sys.argv[1:]   # read all cli args

def merge_pdfs(pdfs):
    merge_obj = PyPDF2.PdfMerger()
    for pdf in pdfs:
        #print(pdf)
        merge_obj.append(pdf)
    merge_obj.write('merged_pdf.pdf')

merge_pdfs(inputs)