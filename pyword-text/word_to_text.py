import docx

doc_file = docx.Document('file/demo.docx')
print(doc_file.paragraphs[0].text)
