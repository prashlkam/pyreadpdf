import os

import gettextfrompdf as reader
import lsdir
import pytts1

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

def main():
    screen_clear()
    print(prompts[0])
    pytts1.textToSpeach(prompts[0])
    pytts1.textToSpeach(prompts[1])
    path = input(prompts[1])
    try:
        if not os.path.isdir(path):
            raise NotADirectoryError
        lstfiles = lsdir.lsdir(path)
        if lstfiles == []:
            print(prompts[3])
            pytts1.textToSpeach(prompts[3])
            raise FileNotFoundError
        else:
            # file to read
            print(prompts[2])
            pytts1.textToSpeach(prompts[2])
            lstfilesmsg = []
            msg1 = 'Press | '
            for fl in lstfiles:
                lstfilesmsg.append(str(lstfiles.index(fl) + 1) + ' for ' + fl + ' | ')
            for lfm in lstfilesmsg:
                msg1 += lfm
            print(msg1)
            pytts1.textToSpeach(msg1)
            pytts1.textToSpeach(prompts[4])
            fno = int(input(prompts[4]))
            fltoread = lstfiles[fno - 1]
            print('We will be reading the book ' + fltoread + '...')
            pytts1.textToSpeach('We will be reading the book ' + fltoread)
            # pages to read
            print(prompts[5])
            pytts1.textToSpeach(prompts[5])
            pytts1.textToSpeach(prompts[6])
            pgchoice = int(input(prompts[6]))
            pagestoread = []
            if pgchoice == 1:
                msg2 = prompts[7].replace(' first', '')
                pytts1.textToSpeach(msg2)
                pagestoread.append(int(input(msg2)))
            elif pgchoice == 2:
                pytts1.textToSpeach(prompts[7])
                start = int(input(prompts[7]))
                pytts1.textToSpeach(prompts[8])
                end = int(input(prompts[8]))
                if end < start or start not in range(reader.gettotpgsinbook(fltoread)) or end not in range(reader.gettotpgsinbook(fltoread)):
                    raise ValueError
                for i in range(start, end):
                    pagestoread.append(i)
            elif pgchoice == 3:
                start = 0
                end = reader.gettotpgsinbook(fltoread)
                for i in range(start, end):
                    pagestoread.append(i)
            else:
                raise RuntimeError
        screen_clear()
        print('We will be reading pages ' + str(pagestoread) + ' from the book ' + fltoread + '...')
        pytts1.textToSpeach('We will be reading pages ' + str(pagestoread) + ' from the book ' + fltoread)
        pagesinbooktoread = reader.getTextFromPdf(fltoread, pagestoread)
        # read the pages
        for pg in pagesinbooktoread:
            print('Reading page ' + str(pagesinbooktoread.index(pg)+1) + ' of ' + str(len(pagesinbooktoread)))
            print('---------------------------------------')
            pytts1.textToSpeach('Reading page ' + str(pagesinbooktoread.index(pg)+1) + ' of ' + str(len(pagesinbooktoread)))
            print(pg)
            pytts1.textToSpeach(pg)
    except NotADirectoryError:
        print(err_prompts[0])
        pytts1.textToSpeach(err_prompts[0])
        print(err_prompts[-1])
        pytts1.textToSpeach(err_prompts[-1])
    except FileNotFoundError:
        print(err_prompts[1])
        pytts1.textToSpeach(err_prompts[1])
        print(err_prompts[-1])
        pytts1.textToSpeach(err_prompts[-1])
    except ValueError:
        print(err_prompts[2])
        pytts1.textToSpeach(err_prompts[2])
        print(err_prompts[-1])
        pytts1.textToSpeach(err_prompts[-1])
    except RuntimeError:
        print(err_prompts[-1])
        pytts1.textToSpeach(err_prompts[-1])
    finally:
        print('Done reading.')
        pytts1.textToSpeach('Done reading.')


def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   
main()
