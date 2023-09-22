import PyPDF2
import psycopg2
import requests

def getTextFromPDF(pdffile):
    with open(pdffile, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdffile, strict=False)

        text = []

        for page in reader.pages:
            content = page.extract_text()
            text.append(content)

        return text

def printText():
    extractedText =  getTextFromPDF("PS2356019869693 copy.pdf")
    for text in extractedText:
        print(text)

def postgresConnect():
    connection = psycopg2.connect(host='localhost', user='mauriceaugust', password='Destiny4days', dbname='postgres', port='5432')
    cursor = connection.cursor()
    print(connection)

def makeHttpRequest():
    API_KEY = 'AIzaSyD1Y3hqtMOwKBtoQSltogaN6cFEzlyff6o'
    ENGINE_ID = '26d42802da9b540bb'
    response = requests.get('https://www.googleapis.com/customsearch/v1?key='+API_KEY+'&cx='+ENGINE_ID+'&q=lectures')

    printText()
    
makeHttpRequest()
