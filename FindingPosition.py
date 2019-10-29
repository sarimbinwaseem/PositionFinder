import PyPDF2 
import os
import pickle

# os.system('color 2')
os.system("cls")
print("Written by Sarim Bin Waseem")
print("Github: https://github.com/sarimbinwaseem")
print("Twitter: https://twitter.com/sarimbinwaseem")
print("Facebook: https://www.facebook.com/sarimbinwaseem.102")
print("This is a free software.")
print("")
##################################################################

# ANSI Codes:

red = '\033[31m'
green = '\033[32m'
brown = '\033[33m'
yellow = "\033[1;33m"
orig = "\033[0m"

def check():	
	while True:
		try:	
			obt_number = int(input(brown + "[?] Enter Obtained Marks: " + orig))
			tot_number = int(input(brown + "[?] Enter Total Marks: " + orig))
		except ValueError:
			print(red + "[-] Enter integers... not characters.." + orig)
		else:
			print("")
			noOfNumber = 0
			line = "1 ahead........"
			numb  = []
			# pickle_obj = []
			path = os.getcwd() + '\\Result.pickle'
			file = open(path, "rb")
			pickle_obj = pickle.load(file)
			# print(pickle_obj) 
			words = []
			for w in pickle_obj:
				words.append(w.split())
				# print(words)

			for number in range(obt_number + 1, tot_number):
				ToSearch1 = "(" +str(number) + ")"
				ToSearch2 = "(" +str(number) + "+" 
				ToSearch3 = "(" +str(number) + "^"
					
					
				for worde in words:
					# print(word)
					for word in worde:
						if word.find(ToSearch1) != -1 or word.find(ToSearch2) != -1 or word.find(ToSearch3) != -1:
							print(line, "Scoring: ",number, " having ", round(((number/tot_number)*100),2), '%')
							line = "1 more ahead..."
							noOfNumber += 1
							if number in numb:
								pass
							else:
								numb.append(number)
			file.close()					

			print("")				
			print(green + "[+] Total number of students ahead you : ",noOfNumber)
			print("[+] Your Position is :", len(numb) + 1)
			print("[+] Students with GRACE MARKS and EXTRA MARKS are counted." + orig)
			print("")
			input(brown + "[+] Press ENTER To Run Again.." + orig)
			print("")
			print("")


#########################################################################	
if __name__ == "__main__":	
	while True:

		pathe = os.getcwd() + '\\Result.pickle'
		file = os.path.isfile(pathe)
		if file:  
			
			check()
		else:
			try:
				PDF_File = input(brown + "[?] Enter the path to Result PDF File (Drag and drop may work): " + orig)
				print("")
				pdfFileObj = open(PDF_File, 'rb') 
				pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
			except OSError:
				print(red + "[-] Please choose the correct file type.. i.e .pdf file or change the file name without spaces.. " + orig)
			except FileNotFoundError:
				print(red + "[-] File Doesn't exist...!! or change the file name without spaces.. "  + orig)
			except:
				print(red + "[!] Please choose the correct file type or contact developer.")	



			else:  
			# printing number of pages in pdf file 
				pages  = int(pdfReader.numPages)
				print(brown + "[+] Total number of pages in PDF:", pages, orig) 
				print("")
				pageObj = pdfReader.getPage(0)
				extracted_text = []

				with open("Result.pickle", "wb") as R_txt:
					for i in range(pages): 	
						# creating a page object 
						pageObj = pdfReader.getPage(i)  
						text = pageObj.extractText()
						extracted_text.append(text)
						
					pickle.dump(extracted_text, R_txt)	
					# print(extracted_text)
				pdfFileObj.close()
				check()

			##################################################################################



