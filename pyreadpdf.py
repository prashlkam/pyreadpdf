# Import the required module for text 
# to speech conversion 
import PyPDF2 
import pyttsx3
import os
from sys import platform

# path for lsdir function
path = 'c:\\projects\\hc2\\'

# The text that you want to convert to audio 
mytext = 'Welcome to Saksham Code Camp! We encourage you to learn coding to try and solve some real world problems.'

# Language in which you want to convert 
language = 'en'

# prompts for main function
prompts = ['Pyreadpdf - A program that reads out text from a pdf file...',
           'Enter path of pdf file you wish to read.: ',
           'Pdf files in this directory are... ', 'There are no pdf files here.',
           'Which pdf file do you want to read? ',
           'Do you want to read one page or multiple pages? ', 'Press 1 for single page, 2 for a range of pages or 3 for the entire book.: ',
           'Enter the number of the first page you want to read.: ', 'Enter the number of the last page you want to read.: ']

err_prompts = ['Not a directory error.',
               'File not found error.',
               'Value error.',
               'Error: Something went wrong. Please relaunch program and try again...']

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 

# create a function
def textToSpeach(mytext):
	# init tts engine
	engine = pyttsx3.init()
	# speak out text
	engine.say(mytext)
	# gracefully exit
	engine.runAndWait()

def textToMp3file(mytext, mp3filname):
	# init tts engine
	engine = pyttsx3.init()
	# check and replace file extension
	mp3filname.replace('.mp3', '')
	# Saving the converted audio in a mp3 file
	engine.save_to_file(mytext,mp3filname + '.mp3')
	# check os / platform
	if platform == "linux" or platform == "linux2":
		# Playing the converted file (linux)
		os.system("plaympeg " + mp3filname + ".mp3")
	elif platform == "win32":
	 	# Windows...
		os.system("start " + mp3filname + ".mp3")
	elif platform == "darwin":
	 	# Mac os...
		pass
	else:
		# other os
		pass
	engine.runAndWait()

def lsdir (path):
	files = []
	# r=root, d=directories, f = files
	for r, d, f in os.walk(path):
		for file in f:
			if '.pdf' in file:
				files.append(os.path.join(r, file))
	for f in files:
		print(f)
	return files


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

def main():
    screen_clear()
    print(prompts[0])
    textToSpeach(prompts[0])
    textToSpeach(prompts[1])
    path = input(prompts[1])
    try:
        if not os.path.isdir(path):
            raise NotADirectoryError
        lstfiles = lsdir(path)
        if lstfiles == []:
            print(prompts[3])
            textToSpeach(prompts[3])
            raise FileNotFoundError
        else:
            # file to read
            print(prompts[2])
            textToSpeach(prompts[2])
            lstfilesmsg = []
            msg1 = 'Press | '
            for fl in lstfiles:
                lstfilesmsg.append(str(lstfiles.index(fl) + 1) + ' for ' + fl + ' | ')
            for lfm in lstfilesmsg:
                msg1 += lfm
            print(msg1)
            textToSpeach(msg1)
            textToSpeach(prompts[4])
            fno = int(input(prompts[4]))
            fltoread = lstfiles[fno - 1]
            print('We will be reading the book ' + fltoread + '...')
            textToSpeach('We will be reading the book ' + fltoread)
            # pages to read
            print(prompts[5])
            textToSpeach(prompts[5])
            textToSpeach(prompts[6])
            pgchoice = int(input(prompts[6]))
            pagestoread = []
            if pgchoice == 1:
                msg2 = prompts[7].replace(' first', '')
                textToSpeach(msg2)
                pagestoread.append(int(input(msg2)))
            elif pgchoice == 2:
                textToSpeach(prompts[7])
                start = int(input(prompts[7]))
                textToSpeach(prompts[8])
                end = int(input(prompts[8]))
                if end < start or start not in range(reader.gettotpgsinbook(fltoread)) or end not in range(reader.gettotpgsinbook(fltoread)):
                    raise ValueError
                for i in range(start, end):
                    pagestoread.append(i)
            elif pgchoice == 3:
                start = 0
                end = gettotpgsinbook(fltoread)
                for i in range(start, end):
                    pagestoread.append(i)
            else:
                raise RuntimeError
        screen_clear()
        print('We will be reading pages ' + str(pagestoread) + ' from the book ' + fltoread + '...')
        textToSpeach('We will be reading pages ' + str(pagestoread) + ' from the book ' + fltoread)
        pagesinbooktoread = getTextFromPdf(fltoread, pagestoread)
        # read the pages
        for pg in pagesinbooktoread:
            print('Reading page ' + str(pagesinbooktoread.index(pg)+1) + ' of ' + str(len(pagesinbooktoread)))
            print('---------------------------------------')
            textToSpeach('Reading page ' + str(pagesinbooktoread.index(pg)+1) + ' of ' + str(len(pagesinbooktoread)))
            print(pg)
            textToSpeach(pg)
    except NotADirectoryError:
        print(err_prompts[0])
        textToSpeach(err_prompts[0])
        print(err_prompts[-1])
        textToSpeach(err_prompts[-1])
    except FileNotFoundError:
        print(err_prompts[1])
        textToSpeach(err_prompts[1])
        print(err_prompts[-1])
        textToSpeach(err_prompts[-1])
    except ValueError:
        print(err_prompts[2])
        textToSpeach(err_prompts[2])
        print(err_prompts[-1])
        textToSpeach(err_prompts[-1])
    except RuntimeError:
        print(err_prompts[-1])
        textToSpeach(err_prompts[-1])
    finally:
        print('Done reading.')
        textToSpeach('Done reading.')


def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   
main()
