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
		
