# Copyright (C) 2018  Dakota Fulp <dkfulp@coastal.edu>
#
# This file is part of pula.
#
# Pula is free software; you can redistribute it and/or modify it under the
# terms of the MIT License.
#
# Pula is distributed in the hope that it will be useful and convienient, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY 
# or FITNESS FOR A PARTICULAR PURPOSE.  See the MIT Licesne for more details.
import os
import csv

#Function: get_file_paths_in_directory(directory)
#Function that takes in a directory and will return all file paths of the directory.
#This also cascades and will not stop at top directory.
def get_file_paths_in_directory(directory):
	return [val for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk(directory)] for val in sublist]

#Function: get_file_names_in_directory(directory)
#Function that takes in a directory and will return a list of all file names in the given directory.
#This also cascades and will not stop at top directory.
def get_file_names_in_directory(directory):
    name_array = []
    for root,dirs,files in os.walk(directory):
        for file in files:
            name_array.append(file)
    return name_array

#Function: print_file_paths_in_directory(directory)
#Function that takes in a directory and will print all file paths of the directory.
#This also cascades and will not stop at top directory.
def print_file_paths_in_directory(directory):
	file_paths = get_filePaths_in_directory(directory)
	for path in file_paths:
		print("File Path = {}".format(path))

#Function: print_file_names_in_directory(directory)
#Function that takes in a directory and will return a list of all file names in the given directory.
#This also cascades and will not stop at top directory.
def print_file_names_in_directory(directory):
	file_names = get_file_names_in_directory(directory)
	for name in file_names:
		print("File Name = %s".format(name))
	

#Function: get_line_contents_and_write(filePaths, csv)
#Function that gets each files line content and line number and writes it out to the given csv.
#This is similar to a file scraping tool.
def get_line_contents_and_write(filePaths, csv):	
	for path in filePaths:
		try:
			#Read each line of filePaths[i]
			file = open(path,"r")
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
