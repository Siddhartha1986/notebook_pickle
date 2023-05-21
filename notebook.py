	
import pickle
import time

count = 0

try:
	filehandle = open("notebook.dat","rb")
	pickle.load(filehandle)
	filehandle.close()
except IOError:
	filehandle = open("notebook.dat","wb")
	#pickle.dump([],filehandle)
	print("No default notebook was found, created one.")
	filehandle.close()



while True:
		
	print("(1) Read the notebook")
	print("(2) Add note")
	print("(3) Edit a note")
	print("(4) Delete a note")
	print("(5) Save and quit")
	
	select = int(input("Please select one:"))
	
	if select == 1:
		try:
			readfile = open("notebook.dat","rb")
			content = pickle.load(readfile)
			#for i in content:
				#print(i,end="")
			print(content)
			print("\n")
			readfile.close()
		except EOFError:
			pass
	
	if select == 2:
		count = count + 1
		addfile = open("notebook.dat","ab")
		newnote = input("Write a new note:")
		
		
		time_date = time.strftime("%X %x")
		new =newnote +":::"+str(time_date)
		news = [new]
		pickle.dump(news,addfile)
		
		addfile.close()
	
	if select ==3:
		editfile = open("notebook.dat","rb")
		econtent = pickle.load(editfile)
		
		print("The list has",count,"notes.")
		choose = int(input("Which of them will be changed?:"))
		print(econtent)
		editfile.close()
		
		new_note = input("Give the new note:")
		filehandle3 = open("notebook.dat","wb")
		time_date = time.strftime("%X %x")
		new =new_note +":::"+str(time_date)
		pickle.dump(new,filehandle3)
		
		
		filehandle3.close()
		
	if select == 4:
		
		print("The list has",count,"notes.")
		delete_choice = int(input("which of them will be deleted?:"))
		
		openfile4 = open("notebook.dat","rb")
		content4 = pickle.load(openfile4)
		print("Deleted note",content4)
		openfile4.close()
		
		deletefile = open("notebook.dat","wb")
		pickle.dump([],deletefile)
		deletefile.close
	
	if select == 5:
		print("Notebook shutting down, thank you.")
		
		
		
		break
		
		
		
		
		
		
		

		
					 
		
	