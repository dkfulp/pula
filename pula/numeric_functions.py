#Function: is_number(num)
#Boolean function that checks to see if value is a number or string
def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
