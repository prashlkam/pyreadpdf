# importing required modules 
import PyPDF2 

# create a function
def getTextFromPdf(flname, pages):
	# creating a pdf file object 
	pdfFileObj = open(flname, 'rb') 
	# creating a pdf reader object 
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
	# printing number of pages in pdf file 
	totalpages = pdfReader.numPages
	Texttoread = []
	# check if pages are in range
	if pageswithinrange(totalpages, pages) == True:
		# loop through pages
		for pg in pages:
			# creating a page object 
			pageObj = pdfReader.getPage(pg) 
			# extracting text from page 
			Texttoread.append(pageObj.extractText())
	else:
		# error message
		print('something went wrong...')
	# closing the pdf file object 
	pdfFileObj.close()
	# return text to read
	return Texttoread

def pageswithinrange(totalpages, pages):
	res = False
	for pg in pages:
		if pg in range(0, totalpages):
			res = True
			continue
		else:
			res = False
			break
	return res

def gettotpgsinbook(fname):
	# creating a pdf file object
	pdfFileObj = open(fname, 'rb')
	# creating a pdf reader object
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	# printing number of pages in pdf file
	totalpages = pdfReader.numPages
	return totalpages


# getTextFromPdf('./data/Manjaro-User-Guide.pdf', [18, 29, 30])
