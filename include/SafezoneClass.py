import include.simplemath
import include.convert

class SafeZone:
	def __init(self):
		path = os.path.dirname(__file__)
		#global backercard_width, box_connector, box_height, page_width, page_lenght, page_margin, page_margin_bottom 
	 
	def getSafeZoneSVG(self, backercard_width, backercard_lenght, box_connector, box_height, page_width, page_lenght, page_margin, page_margin_bottom, fold_1, fold_2): 
		#global backercard_width, box_connector, box_height, page_width, page_lenght, page_margin, page_margin_bottom 
	
		#NAME SHORTENING FOR IMPORTED FUNCTIONS
		mm2px = include.convert.mm2px
		mm_to_pixels = include.convert.mm_to_pixels
		get_initial_pos_x = include.convert.get_initial_pos_x
		set_to_center = include.convert.set_to_center
		get_left_and_right_position = include.convert.get_left_and_right_position
		
		#BOX ELEMENTS GROUP 1
		panel_1 = [(backercard_width+32)-(float(box_connector[0])*2), box_height]
		flap_1 = flap_2 = [box_height*0.85, box_height]
		group_1 = [float(flap_1[0])+float(flap_2[0])+float(panel_1[0]), box_height]
		
		#BOX ELEMENTS GROUP 2
		panel_2 = [backercard_width+32, backercard_lenght+7]
		flap_3 = flap_4 = flap_5 = flap_6 = [box_height, panel_2[1]]
		group_2 = [float(panel_2[0])+(float(flap_3[0])*4)+(float(box_connector[0])*4), float(panel_2[1])]
	
		#BOX ELEMENTS GROUP 3
		panel_3 = [panel_2[0], box_height]
		flap_7 = flap_8 = [(float(flap_1[0])-float(box_connector[0])), box_height]
		group_3 = [float(panel_3[0])+(float(flap_7[0])*2), box_height]
	
		#BOX ELEMENTS GROUP 4
		panel_4 = [panel_1[0], backercard_lenght+17]
		flap_9 = flap_10 = [flap_1[0], panel_4[1]]
		group_4 = [float(panel_4[0])+(float(flap_9[0])*2), panel_4[1]]
	
		#BOX ELEMENTS GROUP 5
		panel_5 = [panel_3[0], box_height]
		flap_11 = flap_12 = [box_height*0.715, panel_5[1]]
		group_5 = [float(flap_11[0])*2+panel_5[0], panel_5[1]]
		
		page_width_in_pixels = mm2px(page_width)
		page_lenght_in_pixels = mm2px(page_lenght)    
		
		#SET INITIAL POSITION FOR PLACEMENT OF THE ELEMENTS
		pos_x = get_initial_pos_x(group_1[0], page_width)
		pos_y = mm_to_pixels(page_margin)
			
		#WRITE SVG BASE CODE
		svg_code = f'<?xml version="1.0" encoding="UTF-8"?><svg version="1.1" id="SafeZone" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="{page_width_in_pixels}" height="{page_lenght_in_pixels}" viewBox="0 0 {page_width_in_pixels} {page_lenght_in_pixels}">'  
   	
		#PANEL_ONE
		p_one = set_to_center(group_1[0], group_1[1], pos_x, pos_y)   
		
		###GROUP 1
		#ARRAY WITH [TOP Y POSITION, BOTTOM Y POSITION] AND [LEFT X POSITION, RIGHT X POSITION] 
		group_y = [p_one[1], pos_y+mm_to_pixels(group_1[1])]
		group_x = [p_one[0], pos_x]       
		
		svg_code += f'<rect id="ATM-PANEL-01" name="ATMN-PANEL-01" class="ATMC-PANEL-01" x="{float(p_one[0])+mm_to_pixels(flap_1[0]+10)}" y="{float(p_one[1])+mm2px(10)}" width="{mm_to_pixels(float(panel_1[0])-20)}" height="{mm_to_pixels(float(panel_1[1])-20)}" stroke="#EC008C"  fill="none" stroke-width="2px"/>'
  	
		###GROUP 2
		#ARRAY WITH [TOP Y POSITION, BOTTOM Y POSITION] AND [LEFT X POSITION, RIGHT X POSITION] 
		group_y = [group_y[1], group_y[1]+mm_to_pixels(group_2[1])]
		group_x = get_left_and_right_position(group_2, page_width)  
  	
		svg_code += f'<rect id="ATM-FLAP-04" x="{float(group_x[0])+mm_to_pixels(float(box_connector[0])+float(flap_3[0])+fold_1+10)}" y="{float(group_y[0])+mm2px(10)}" width="{mm_to_pixels(float(flap_4[0])-20)}" height="{mm_to_pixels(float(flap_4[1])-20)}" stroke="#EC008C"  fill="none" stroke-width="2px"/>'
		svg_code += f'<rect id="ATM-PANEL-02" x="{float(group_x[0])+mm_to_pixels(float(box_connector[0])+float(flap_3[0])*2+fold_1+15)}" y="{float(group_y[0])+mm2px(15)}" width="{mm_to_pixels(float(panel_2[0])-30)}" height="{mm_to_pixels(float(panel_2[1])-30)}" stroke="#EC008C"  fill="none" stroke-width="2px"/>'
		svg_code += f'<rect id="ATM-FLAP-05" x="{float(group_x[1])-mm_to_pixels(float(box_connector[0])+float(flap_5[0])*2+(fold_2)-10)}" y="{float(group_y[0])+mm2px(10)}" width="{mm_to_pixels(float(flap_4[0])-20)}" height="{mm_to_pixels(float(flap_4[1])-20)}" stroke="#EC008C"  fill="none" stroke-width="2px"/>'
	
		###GROUP 3
		#ARRAY WITH [TOP Y POSITION, BOTTOM Y POSITION] AND [LEFT X POSITION, RIGHT X POSITION] 
		group_y = [group_y[1], group_y[1]+mm_to_pixels(group_3[1])]
		group_x = get_left_and_right_position(group_3, page_width)    
	
		svg_code += f'<rect id="ATM-PANEL-03" x="{float(group_x[0])+mm2px(float(flap_7[0])+10)}" y="{float(group_y[0])+mm2px(10)}" width="{mm_to_pixels(float(panel_3[0])-20)}" height="{mm_to_pixels(float(panel_3[1])-20)}" stroke="#EC008C"  fill="none" stroke-width="2px"/>'    
		
		###GROUP 4
		#ARRAY WITH [TOP Y POSITION, BOTTOM Y POSITION] AND [LEFT X POSITION, RIGHT X POSITION] 
		group_y = [group_y[1], group_y[1]+mm_to_pixels(group_4[1])]
		group_x = get_left_and_right_position(group_4, page_width)    
		
		svg_code += f'<rect id="ATM-PANEL-04" x="{float(group_x[0])+mm2px(float(flap_9[0])+10)}" y="{float(group_y[0])+mm2px(10)}" width="{mm_to_pixels(float(panel_4[0])-20)}" height="{mm_to_pixels(float(panel_4[1])-20)}" stroke="#EC008C"  fill="none" stroke-width="2px"/>'        
	 	
		###GROUP 5
		#ARRAY WITH [TOP Y POSITION, BOTTOM Y POSITION] AND [LEFT X POSITION, RIGHT X POSITION] 
		group_y = [group_y[1], group_y[1]+mm_to_pixels(group_5[1])]
		group_x = get_left_and_right_position(group_5, page_width)
	 	
		svg_code += f'<rect id="ATM-PANEL-05" x="{float(group_x[0])+mm2px(float(flap_11[0])+10)}" y="{float(group_y[0]+mm2px(10))}" width="{mm_to_pixels(float(panel_5[0])-20)}" height="{mm_to_pixels(float(panel_5[1])-20)}" stroke="#EC008C"  fill="none" stroke-width="2px"/>'
			
		#CREATE OUT MARGIN THE SIZE OF THE PAGE
		
		svg_code += f'<rect id="ATM-SZ-PAGE" x="0" y="0" width="{page_width_in_pixels}" height="{page_lenght_in_pixels}" stroke="#ffffff"  fill="none" stroke-width="1px"/>'
		
		svg_code += f'</svg>' 
	
		return svg_code