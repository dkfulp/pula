import os
import csv

#Function: get_filePaths_in_directory(directory)
#Function that takes in a directory and will return all filePaths of the directory
def get_filePaths_in_directory(directory):
	return [val for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk(directory)] for val in sublist]

#Function: get_line_contents_and_write(filePaths, csv)
#Function that gets each files line content and line number and writes it out to the given csv
def get_line_contents_and_write(filePaths, csv):	
	for path in filePaths:
		try:
			#Read each line of filePaths[i]
			file = open(path,"r")
			if path.endswith(('.c','.h','.S')):
				i = 1
				for line in file:
					#sanitize file (take out commas that mess with delimiter)
					line = re.sub('[^A-Za-z0-9]+', ' ', line)
					if line	!= " ":			
						csv.write(path+","+str(i)+","+line+"\n")
					i = i + 1
		except FileNotFoundError:
			print(path + ": File is Empty . . . Skipping")
		except UnicodeDecodeError:
			print(path + ": Cannot Read File (UnicodeDecodeError) . . . Attempting to Convert", end = " . . . ")
			try:
				file = open(path,"r", encoding = 'iso-8859-1')
				print("Successfully Converted!")
				if path.endswith(('.c', '.h','.S')):
					i = 1
					for line in file:
						#sanitize file (take out commas that mess with delimiter)
						line = re.sub('[^A-Za-z0-9]+', ' ', line)
						if line	!= " ":			
							csv.write(path+","+str(i)+","+line+"\n")
						i = i + 1
			except:
				print("Unable to Convert . . . Skipping")
