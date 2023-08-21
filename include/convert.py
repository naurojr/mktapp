import sys

#sku = "LW070820" #@param {type: "string"}
#@markdown ---
#is_piece_measurement = True   #@param {type:"boolean"}
#@markdown Check if measurements are for piece, otherwise inform box outside measurments
#@markdown ---

#unit_of_measurement = "mm" #@param ["inches", "mm"]
#mosaic_width = 325  #@param {type:"number"}
#mosaic_lenght = 200  #@param {type:"number"}
#mosaic_height = 6  #@param {type:"number"}
#pieces_per_box = 11  #@param {type:"number"}
#need_backercard = True   #@param {type:"boolean"}
#window = True   #@param {type:"boolean"}

#FUNCTION TO CONVERT NUMBER FROM MM TO PIXELS
def mm_to_pixels(number):
	return number*2.83465

#SHORT VERSION OF mm_to_pixels FUNCTION 
def mm2px(number):
	return mm_to_pixels(number)  

#SET OBJECT TO CENTER BASED ON PAGE SIZE, OBJECT SIZE AND PAST INDEX
def set_to_center(obj_width, obj_lenght, x, y):
	global pos_x, pos_y
    
	pos_x = mm_to_pixels(obj_width)+x;
	pos_y = y;
	
	return [x, y, obj_width, obj_lenght]

#CALCULATE LEFT AND RIGHT POSITION FOR GROUPS
def get_left_and_right_position(group, page_width):
	#global page_width
	
	left = get_initial_pos_x(float(group[0]), page_width)
	right = left+mm2px(float(group[0]))
    
	return [left, right]
	
#GET INITIAL POSITION X FOR A ROW BASED ON THE SIZE OF THE PAGE AND ROW
	#RETURN X IN PIXELS
def get_initial_pos_x(row, the_page_width = ""):
	#if page_width not provided use global page width
	if not the_page_width:
		global page_width 
		page = page_width
	else:
		page = the_page_width
		
	return mm_to_pixels((page/2)-(row/2))