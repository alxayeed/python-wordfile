import docx
import logging

logger = logging.getLogger('py-word   ')
logger.setLevel(level=logging.DEBUG)


doc_file = docx.Document('file/demo.docx')

paragraphs = doc_file.paragraphs
# get number of paragraph in the word file
logging.info(f'Total paragraph : {len(paragraphs)}')

# print all paragraphs text
for p in paragraphs:
    logger.info(p.text)

# Runs means different format of text, eg- normal, bold, italic etc
# print runs
logger.info(paragraphs[2].runs[1].text)
