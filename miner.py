import pdfminer

from pdfminer.high_level import extract_text
text = extract_text('data/monopoly.pdf')
print(repr(text))