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


#Function: is_number(num)
#Boolean function that checks to see if value is a number or string

import re
def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def is_integer(num):
	try:
		if float(num).is_integer():
			return True
		else:
			return False
	except:
		return False
		

def string_to_numeric_array(string):
	converted_array = []
	positions = re.findall('\d+',string)
	for j in range(len(positions)):
		if is_number(positions[j]) == True:
			converted_array.append(int(positions[j]))
		else:
			converted_array.append(positions[j])
	return converted_array