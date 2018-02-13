#!/usr/bin/env python
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import sys

pdf_path = sys.argv[1]



rsrcmgr = PDFResourceManager()
rettxt = StringIO()
laparams = LAParams()

device = TextConverter(rsrcmgr, rettxt, codec='utf-8', laparams=laparams)
with open(pdf_path, 'rb') as fp:
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(fp, pagenos=None, maxpages=0, password=None, caching=True, check_extractable=True):
        interpreter.process_page(page)

    text = rettxt.getvalue()
    text = text.split('Abstract')[1]
    text = text.replace('\n', ' ')
    text = text.replace('  ', '\n')

    device.close()
    rettxt.close()
# 彼女氏のいたずらコード
new_file_name = pdf_path + '.txt'
with  open(new_file_name, 'w') as f:
    f.write(text)

