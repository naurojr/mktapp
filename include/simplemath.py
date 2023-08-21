import math, time, os


def truncate(f, n):
	return math.floor(f * 10 ** n) / 10 ** n

def normalize_number(number, decimals):
	new_number = truncate(number, decimals)
	
	if((int(new_number) - new_number) == 0):
		new_number = int(new_number)
		
	return new_number;