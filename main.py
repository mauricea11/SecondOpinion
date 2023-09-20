import PyPDF2

def getTextFromPDF(pdffile):
    with open(pdffile, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdffile, strict=False)

        text = []

        for page in reader.pages:
            content = page.extract_text()
            text.append(content)

        return text

extractedText =  getTextFromPDF("PS2356019869693 copy.pdf")

for text in extractedText:
    print(text)