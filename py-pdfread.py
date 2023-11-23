from pdfquery import PDFQuery
import pandas as pd
import pdfquery


pdf = PDFQuery('Book Digital G.M. ok copy.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal' )

# Extract the text from the elements
text = [t.text for t in text_elements]

"""print(text)
sourceFile = open('demo.txt','w')
print(text, file = sourceFile)
sourceFile.close()"""