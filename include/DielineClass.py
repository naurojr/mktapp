import os
import include.simplemath
import include.convert
import include.GetFooter


class Dieline:

	def __init__(self):
		path = os.path.dirname(__file__)
		#global backercard_width, box_connector, box_height, page_width, page_lenght, page_margin, page_margin_bottom 
	
	def getDielineSVG(self, backercard_width, backercard_lenght, box_connector, box_height, page_width, page_lenght, page_margin, page_margin_bottom, window, version, sku, base_name, fold_1, fold_2):
		#global backercard_width, box_connector, box_height, page_width, page_lenght, page_margin, page_margin_bottom, window, version, sku, base_name     
		#file_name = os.path.splitext(os.path.basename(the_file))[0]
		
		#NAME SHORTENING FOR IMPORTED FUNCTIONS
		mm2px = include.convert.mm2px
		mm_to_pixels = include.convert.mm_to_pixels
		get_initial_pos_x = include.convert.get_initial_pos_x
		set_to_center = include.convert.set_to_center
		get_left_and_right_position = include.convert.get_left_and_right_position
		get_footer = include.GetFooter.get_footer
		
		
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
		
		#CONVERT PAGE DIMENSIONS TO PIXEL
		page_width_in_pixels = mm2px(page_width)
		page_lenght_in_pixels = mm2px(page_lenght)    
		
		#SET INITIAL POSITION FOR PLACEMENT OF THE ELEMENTS
		pos_x = get_initial_pos_x(group_1[0], page_width)
		pos_y = mm_to_pixels(page_margin) 
		
		
		#WRITE SVG BASE CODE
		svg_code = f'<svg width="{page_width_in_pixels}" height="{page_lenght_in_pixels}" viewBox="0 0 {page_width_in_pixels} {page_lenght_in_pixels}">'  
		
		
		#PANEL_ONE
		p_one = set_to_center(group_1[0], group_1[1], pos_x, pos_y)    
		#svg_code += f'<rect x="{p_one[0]}" y="{p_one[1]}" width="{mm_to_pixels(p_one[2])}" height="{mm_to_pixels(p_one[3])}" stroke="#00aeef"  fill="none" stroke-width="2px"/>'
	
		###GROUP 1
		#ARRAY WITH [TOP Y POSITION, BOTTOM Y POSITION] AND [LEFT X POSITION, RIGHT X POSITION] 
		group_y = [p_one[1], pos_y+mm_to_pixels(group_1[1])]
		group_x = [p_one[0], pos_x+mm2px(group_1[0])]
	
	
		#GROUP ONE DASHED LINES
		svg_code += f'<line x1="{float(p_one[0])+mm_to_pixels(flap_1[0])}" x2="{float(p_one[0])+mm_to_pixels(flap_1[0])}" y1="{group_y[0]}" y2="{group_y[1]}" stroke="#00aeef" stroke-dasharray="15" stroke-width="2px"/>'
		svg_code += f'<line x1="{float(p_one[0])+mm_to_pixels(flap_1[0])+mm_to_pixels(panel_1[0])}" x2="{float(p_one[0])+mm_to_pixels(flap_1[0])+mm_to_pixels(panel_1[0])}" y1="{group_y[0]}" y2="{group_y[1]}" stroke="#00aeef" stroke-dasharray="15" stroke-width="2px"/>'
	
		#SET POLYLINE INITAL POSITION FOR EASY USE ON CALCULATION OF OTHER POINTS
		poly_init_pos = [p_one[0]+mm_to_pixels(flap_1[0]), pos_y+mm_to_pixels(group_1[1])]
	
		#SET ARRAY OF POINTS FOR POLYLINE
		poly_points = [f'{poly_init_pos[0]},{poly_init_pos[1]}']
		poly_points.append(f'{poly_init_pos[0]-mm2px(float(box_connector[0]))},{poly_init_pos[1]-mm2px(float(box_connector[0]))}')
		poly_points.append(f'{group_x[0]},{poly_init_pos[1]-mm2px(float(box_connector[0]))}')
		poly_points.append(f'{group_x[0]},{group_y[0]+mm2px(float(box_connector[0]))}')
		poly_points.append(f'{poly_init_pos[0]-mm2px(float(box_connector[0]))},{group_y[0]+mm2px(float(box_connector[0]))}')
		poly_points.append(f'{poly_init_pos[0]},{group_y[0]}')
	
		#BOX ACCESS TO TILE
		poly_points.append(f'{poly_init_pos[0]+(mm2px(panel_1[0])*.27)},{group_y[0]}')
		poly_points.append(f'{poly_init_pos[0]+(mm2px(panel_1[0])*.30)},{float(group_y[1])*0.55}')
		poly_points.append(f'{poly_init_pos[0]+(mm2px(panel_1[0])*.70)},{float(group_y[1])*0.55}')
		poly_points.append(f'{poly_init_pos[0]+(mm2px(panel_1[0])*.73)},{group_y[0]}')
		poly_points.append(f'{poly_init_pos[0]+(mm2px(panel_1[0]))},{group_y[0]}')
	
		
		poly_points.append(f'{(float(group_x[1])-mm2px(flap_2[0]))+mm2px(float(box_connector[0]))},{group_y[0]+mm2px(float(box_connector[0]))}')
   	
		
		poly_points.append(f'{group_x[1]},{group_y[0]+mm2px(float(box_connector[0]))}')
		poly_points.append(f'{group_x[1]},{group_y[1]-mm2px(float(box_connector[0]))}')
		poly_points.append(f'{(group_x[1]-mm2px(flap_2[0]))+mm2px(float(box_connector[0]))},{group_y[1]-mm2px(float(box_connector[0]))}')
		poly_points.append(f'{(group_x[1]-mm2px(flap_2[0]))},{group_y[1]}')
	
		#EXPLODE POLY POINTS ARRAY INTO STRING 
		poly_string = " "
		poly_string = poly_string.join(poly_points)
	
		#GROUP POLYLINE GROUP 1
		svg_code += f'<polyline points="{poly_string}" stroke="#00aeef" fill="none" stroke-width="2"/>'
	
		###GROUP 2
		#ARRAY WITH [TOP Y POSITION, BOTTOM Y POSITION] AND [LEFT X POSITION, RIGHT X POSITION] 
		group_y = [group_y[1], group_y[1]+mm_to_pixels(group_2[1])]
		group_x = get_left_and_right_position(group_2, page_width)
	
		#GROUP ONE DASHED LINES
		svg_code += f'<line x1="{float(group_x[0])+mm_to_pixels(float(box_connector[0])+float(flap_3[0]))}" x2="{float(group_x[0])+mm_to_pixels(float(box_connector[0])+float(flap_3[0]))}" y1="{group_y[0]}" y2="{group_y[1]}" stroke="#00aeef" stroke-dasharray="15" stroke-width="2px"/>'
		svg_code += f'<line x1="{float(group_x[0])+mm_to_pixels(float(box_connector[0])+float(flap_3[0])+fold_1)}" x2="{float(group_x[0])+mm_to_pixels(float(box_connector[0])+float(flap_3[0])+fold_1)}" y1="{group_y[0]}" y2="{group_y[1]}" stroke="#00aeef" stroke-dasharray="15" stroke-width="2px"/>'
		svg_code += f'<line x1="{float(group_x[0])+mm_to_pixels(float(box_connector[0])+float(flap_3[0])*2+fold_1)}" x2="{float(group_x[0])+mm_to_pixels(float(box_connector[0])+float(flap_3[0])*2+fold_1)}" y1="{group_y[0]}" y2="{group_y[1]}" stroke="#00aeef" stroke-dasharray="15" stroke-width="2px"/>'
	
		svg_code += f'<line x1="{float(group_x[0])+mm_to_pixels(float(box_connector[0])+float(flap_3[0])*2+fold_1)}" x2="{float(group_x[1])-mm_to_pixels(float(box_connector[0])+float(flap_5[0])*2+fold_2)}" y1="{group_y[0]}" y2="{group_y[0]}" stroke="#00aeef" stroke-dasharray="15" stroke-width="2px"/>'
		svg_code += f'<line x1="{float(group_x[0])+mm_to_pixels(float(box_connector[0])+float(flap_3[0])*2+fold_1)}" x2="{float(group_x[1])-mm_to_pixels(float(box_connector[0])+float(flap_5[0])*2+fold_2)}" y1="{group_y[1]}" y2="{group_y[1]}" stroke="#00aeef" stroke-dasharray="15" stroke-width="2px"/>'
	
		svg_code += f'<line x1="{float(group_x[1])-mm_to_pixels(float(box_connector[0])+float(flap_5[0])*2+fold_2)}" x2="{float(group_x[1])-mm_to_pixels(float(box_connector[0])+float(flap_5[0])*2+fold_2)}" y1="{group_y[0]}" y2="{group_y[1]}" stroke="#00aeef" stroke-dasharray="15" stroke-width="2px"/>'
		svg_code += f'<line x1="{float(group_x[1])-mm_to_pixels(float(box_connector[0])+float(flap_5[0])+fold_2)}" x2="{float(group_x[1])-mm_to_pixels(float(box_connector[0])+float(flap_5[0])+fold_2)}" y1="{group_y[0]}" y2="{group_y[1]}" stroke="#00aeef" stroke-dasharray="15" stroke-width="2px"/>'
		svg_code += f'<line x1="{float(group_x[1])-mm_to_pixels(float(box_connector[0])+float(flap_5[0]))}" x2="{float(group_x[1])-mm_to_pixels(float(box_connector[0])+float(flap_5[0]))}" y1="{group_y[0]}" y2="{group_y[1]}" stroke="#00aeef" stroke-dasharray="15" stroke-width="2px"/>'
	
		#SET POLYLINE INITAL POSITION FOR EASY USE ON CALCULATION OF OTHER POINTS
		poly_init_pos = [float(group_x[0])+mm_to_pixels(float(box_connector[0])+float(flap_3[0])*2+fold_1), group_y[1]]
	
		#SET ARRAY OF POINTS FOR POLYLINE
		poly_points = [f'{poly_init_pos[0]},{poly_init_pos[1]}']
		poly_points.append(f'{group_x[0]+mm2px(float(box_connector[0]))},{poly_init_pos[1]}')
		poly_points.append(f'{group_x[0]+mm2px(float(box_connector[0]))},{poly_init_pos[1]-mm2px(float(group_2[1])*0.22)}')
		poly_points.append(f'{group_x[0]},{poly_init_pos[1]-mm2px(float(group_2[1])*0.22)}')
		poly_points.append(f'{group_x[0]},{poly_init_pos[1]-mm2px(float(group_2[1])*0.36)}')
		poly_points.append(f'{group_x[0]+mm2px(float(box_connector[0]))},{poly_init_pos[1]-mm2px(float(group_2[1])*0.36)}')
		poly_points.append(f'{group_x[0]+mm2px(float(box_connector[0]))},{poly_init_pos[1]-mm2px(float(group_2[1])*0.66)}')
		poly_points.append(f'{group_x[0]},{poly_init_pos[1]-mm2px(float(group_2[1])*0.66)}')
		poly_points.append(f'{group_x[0]},{poly_init_pos[1]-mm2px(float(group_2[1])*0.80)}')
		poly_points.append(f'{group_x[0]+mm2px(float(box_connector[0]))},{poly_init_pos[1]-mm2px(float(group_2[1])*0.80)}')
		poly_points.append(f'{group_x[0]+mm2px(float(box_connector[0]))},{poly_init_pos[1]-mm2px(float(group_2[1]))}')
		poly_points.append(f'{poly_init_pos[0]},{poly_init_pos[1]-mm2px(float(group_2[1]))}')
	
		#EXPLODE POLY POINTS ARRAY INTO STRING 
		poly_string = " "
		poly_string = poly_string.join(poly_points)
	
		#GROUP POLYLINE GROUP 2
		svg_code += f'<polyline points="{poly_string}" stroke="#00aeef" fill="none" stroke-width="2"/>'
	
		#DIECUT FOR BOX CONNECTOR AT BOTTOM OF THE BOX
		svg_code += f'<rect x="{float(group_x[0])+mm_to_pixels(float(box_connector[0])+float(flap_3[0])*2+fold_1)}" y="{poly_init_pos[1]-mm2px(float(group_2[1])*0.80)}" width="{mm2px(box_connector[0])}" height="{mm2px(box_connector[1])}" stroke="#00aeef" fill="none" stroke-width="2px"/>'
		svg_code += f'<rect x="{float(group_x[0])+mm_to_pixels(float(box_connector[0])+float(flap_3[0])*2+fold_1)}" y="{poly_init_pos[1]-mm2px(float(group_2[1])*0.36)}" width="{mm2px(box_connector[0])}" height="{mm2px(box_connector[1])}" stroke="#00aeef" fill="none" stroke-width="2px"/>'
	
		#SET POLYLINE INITAL POSITION FOR EASY USE ON CALCULATION OF OTHER POINTS
		poly_init_pos = [float(group_x[1])-mm_to_pixels(float(box_connector[0])+float(flap_5[0])*2+fold_2), group_y[1]]
	
		poly_points = [f'{poly_init_pos[0]},{poly_init_pos[1]}']
		poly_points.append(f'{group_x[1]-mm2px(float(box_connector[0]))},{poly_init_pos[1]}')
		poly_points.append(f'{group_x[1]-mm2px(float(box_connector[0]))},{poly_init_pos[1]-mm2px(float(group_2[1])*0.22)}')
		poly_points.append(f'{group_x[1]},{poly_init_pos[1]-mm2px(float(group_2[1])*0.22)}')
		poly_points.append(f'{group_x[1]},{poly_init_pos[1]-mm2px(float(group_2[1])*0.36)}')
		poly_points.append(f'{group_x[1]-mm2px(float(box_connector[0]))},{poly_init_pos[1]-mm2px(float(group_2[1])*0.36)}')
		poly_points.append(f'{group_x[1]-mm2px(float(box_connector[0]))},{poly_init_pos[1]-mm2px(float(group_2[1])*0.66)}')
		poly_points.append(f'{group_x[1]},{poly_init_pos[1]-mm2px(float(group_2[1])*0.66)}')
		poly_points.append(f'{group_x[1]},{poly_init_pos[1]-mm2px(float(group_2[1])*0.80)}')
		poly_points.append(f'{group_x[1]-mm2px(float(box_connector[0]))},{poly_init_pos[1]-mm2px(float(group_2[1])*0.80)}')
		poly_points.append(f'{group_x[1]-mm2px(float(box_connector[0]))},{poly_init_pos[1]-mm2px(float(group_2[1]))}')
		poly_points.append(f'{poly_init_pos[0]},{poly_init_pos[1]-mm2px(float(group_2[1]))}')
	
		#EXPLODE POLY POINTS ARRAY INTO STRING 
		poly_string = " "
		poly_string = poly_string.join(poly_points)
	
		#GROUP POLYLINE GROUP 2
		svg_code += f'<polyline points="{poly_string}" stroke="#00aeef" fill="none" stroke-width="2"/>'
	
		#DIECUT FOR BOX CONNECTOR AT BOTTOM OF THE BOX
		svg_code += f'<rect x="{float(group_x[1])-mm_to_pixels(float(box_connector[0])*2+float(flap_3[0])*2+fold_1)}" y="{poly_init_pos[1]-mm2px(float(group_2[1])*0.80)}" width="{mm2px(box_connector[0])}" height="{mm2px(box_connector[1])}" stroke="#00aeef" fill="none" stroke-width="2px"/>'
		svg_code += f'<rect x="{float(group_x[1])-mm_to_pixels(float(box_connector[0])*2+float(flap_3[0])*2+fold_1)}" y="{poly_init_pos[1]-mm2px(float(group_2[1])*0.36)}" width="{mm2px(box_connector[0])}" height="{mm2px(box_connector[1])}" stroke="#00aeef" fill="none" stroke-width="2px"/>'
	
		###GROUP 3
		#ARRAY WITH [TOP Y POSITION, BOTTOM Y POSITION] AND [LEFT X POSITION, RIGHT X POSITION] 
		group_y = [group_y[1], group_y[1]+mm_to_pixels(group_3[1])]
		group_x = get_left_and_right_position(group_3, page_width)
	
		#GROUP THREE DASHED LINES
		svg_code += f'<line x1="{float(group_x[0])+mm2px(float(flap_7[0]))}" x2="{float(group_x[0])+mm2px(float(flap_7[0]))}" y1="{group_y[0]}" y2="{group_y[1]-mm2px(float(box_connector[0]))}" stroke="#00aeef" stroke-dasharray="15" stroke-width="2px"/>'
		svg_code += f'<line x1="{float(group_x[1])-mm2px(float(flap_8[0]))}" x2="{float(group_x[1])-mm2px(float(flap_8[0]))}" y1="{group_y[0]}" y2="{group_y[1]-mm2px(float(box_connector[0]))}" stroke="#00aeef" stroke-dasharray="15" stroke-width="2px"/>'
		svg_code += f'<line x1="{float(group_x[0])+mm2px(flap_7[0])+mm2px(float(box_connector[0]))}" x2="{float(group_x[1])-(mm2px(float(box_connector[0]))+mm2px(flap_7[0]))}" y1="{group_y[1]}" y2="{group_y[1]}" stroke="#00aeef" stroke-dasharray="15" stroke-width="2px"/>'
	
		#SET POLYLINE INITAL POSITION FOR EASY USE ON CALCULATION OF OTHER POINTS
		poly_init_pos = [float(group_x[0])+mm_to_pixels(float(flap_7[0])), group_y[0]]
	
		poly_points = [f'{poly_init_pos[0]},{poly_init_pos[1]}']
		poly_points.append(f'{poly_init_pos[0]-mm2px(float(box_connector[0]))},{poly_init_pos[1]+mm2px(float(box_connector[0]))}')
		poly_points.append(f'{group_x[0]},{poly_init_pos[1]+mm2px(float(box_connector[0]))}')
		poly_points.append(f'{group_x[0]},{group_y[1]-mm2px(float(box_connector[0]))}')
		poly_points.append(f'{group_x[0]+mm2px(flap_7[0])},{group_y[1]-mm2px(float(box_connector[0]))}')
		poly_points.append(f'{group_x[0]+mm2px(flap_7[0])+mm2px(float(box_connector[0]))},{group_y[1]}')
	
		#EXPLODE POLY POINTS ARRAY INTO STRING 
		poly_string = " "
		poly_string = poly_string.join(poly_points)
	
		#GROUP POLYLINE GROUP 3
		svg_code += f'<polyline points="{poly_string}" stroke="#00aeef" fill="none" stroke-width="2"/>'
	
		#SET POLYLINE INITAL POSITION FOR EASY USE ON CALCULATION OF OTHER POINTS
		poly_init_pos = [float(group_x[1])-mm_to_pixels(float(flap_8[0])), group_y[0]]
		poly_points = [f'{poly_init_pos[0]},{poly_init_pos[1]}']
		poly_points.append(f'{poly_init_pos[0]+mm2px(float(box_connector[0]))},{poly_init_pos[1]+mm2px(float(box_connector[0]))}')
		poly_points.append(f'{group_x[1]},{poly_init_pos[1]+mm2px(float(box_connector[0]))}')
		poly_points.append(f'{group_x[1]},{group_y[1]-mm2px(float(box_connector[0]))}')
		poly_points.append(f'{group_x[1]-mm2px(flap_7[0])},{group_y[1]-mm2px(float(box_connector[0]))}')
		poly_points.append(f'{group_x[1]-(mm2px(flap_7[0])+mm2px(float(box_connector[0])))},{group_y[1]}')
	
		#EXPLODE POLY POINTS ARRAY INTO STRING 
		poly_string = " "
		poly_string = poly_string.join(poly_points)
	
		#GROUP POLYLINE GROUP 3
		svg_code += f'<polyline points="{poly_string}" stroke="#00aeef" fill="none" stroke-width="2"/>'
	
		###GROUP 4
		#ARRAY WITH [TOP Y POSITION, BOTTOM Y POSITION] AND [LEFT X POSITION, RIGHT X POSITION] 
		group_y = [group_y[1], group_y[1]+mm_to_pixels(group_4[1])]
		group_x = get_left_and_right_position(group_4, page_width)
	
		#GROUP THREE DASHED LINES
		svg_code += f'<line x1="{float(group_x[0])+mm2px(float(flap_9[0]))}" x2="{float(group_x[0])+mm2px(float(flap_9[0]))}" y1="{group_y[0]}" y2="{group_y[1]}" stroke="#00aeef" stroke-dasharray="15" stroke-width="2px"/>'
		svg_code += f'<line x1="{float(group_x[1])-mm2px(float(flap_10[0]))}" x2="{float(group_x[1])-mm2px(float(flap_10[0]))}" y1="{group_y[0]}" y2="{group_y[1]}" stroke="#00aeef" stroke-dasharray="15" stroke-width="2px"/>'
		svg_code += f'<line x1="{float(group_x[0])+mm2px(float(flap_9[0]))}" x2="{float(group_x[1])-mm2px(float(flap_10[0]))}" y1="{group_y[1]}" y2="{group_y[1]}" stroke="#00aeef" stroke-dasharray="15" stroke-width="2px"/>'
	
		#DRAW WINDOW ON DIELINE IF REQUIRED
		if window: 
			svg_code += f'<rect x="{group_x[1]-(mm2px(flap_10[0])+mm2px(window_size)+mm2px(45))}" y="{float(group_y[0])+(mm2px(float(panel_4[1])/2-window_size/2))}" width="{mm_to_pixels(window_size)}" height="{mm_to_pixels(window_size)}" stroke="#00aeef" fill="none" stroke-width="2px"/>' 
	
		#SET PATHLINE INITAL POSITION FOR EASY USE ON CALCULATION OF OTHER POINTS
		path_init_pos = [float(group_x[0])+mm_to_pixels(float(flap_9[0])), (group_y[0]+mm2px(float(box_connector[0])))]
		path_points = [f'M{path_init_pos[0]},{path_init_pos[1]}']
		path_points.append(f'{float(group_x[0])+mm2px(float(box_connector[0]))},{group_y[0]+mm2px(22)}')
	
		curve_points = [float(group_x[0])-mm2px(1), group_y[0]+mm2px(23)]
		path_points.append(f'Q{str(curve_points[0])},{str(curve_points[1])}')
	
		path_points.append(f'{float(group_x[0])},{group_y[0]+mm2px(30)}')
		path_points.append(f'L{float(group_x[0])},{group_y[1]-mm2px(30)}')
	
		curve_points = [float(group_x[0])-mm2px(1), group_y[1]-mm2px(23)]
		path_points.append(f'Q{str(curve_points[0])},{str(curve_points[1])}')
	
		path_points.append(f'{float(group_x[0])+mm2px(float(box_connector[0]))},{group_y[1]-mm2px(22)}')
		path_points.append(f'L{path_init_pos[0]},{group_y[1]-mm2px(float(box_connector[0]))}')
	
		#EXPLODE POLY POINTS ARRAY INTO STRING 
		path_string = " "
		path_string = path_string.join(path_points)
		
		#GROUP POLYLINE GROUP 4
		svg_code += f'<path d="{path_string}" stroke="#00aeef" fill="none" stroke-width="2"/>'
	
		#SET PATHLINE INITAL POSITION FOR EASY USE ON CALCULATION OF OTHER POINTS
		path_init_pos = [float(group_x[1])-mm_to_pixels(float(flap_10[0])), (group_y[0]+mm2px(float(box_connector[0])))]
	
		path_points = [f'M{path_init_pos[0]},{path_init_pos[1]}']
		path_points.append(f'{float(group_x[1])-mm2px(float(box_connector[0]))},{group_y[0]+mm2px(22)}')
	
		curve_points = [float(group_x[1])+mm2px(1), group_y[0]+mm2px(23)]
		path_points.append(f'Q{str(curve_points[0])},{str(curve_points[1])}')
	
		path_points.append(f'{float(group_x[1])},{group_y[0]+mm2px(30)}')
		path_points.append(f'L{float(group_x[1])},{group_y[1]-mm2px(30)}')
	
		curve_points = [float(group_x[1])+mm2px(1), group_y[1]-mm2px(23)]
		path_points.append(f'Q{str(curve_points[0])},{str(curve_points[1])}')
	
		path_points.append(f'{float(group_x[1])-mm2px(float(box_connector[0]))},{group_y[1]-mm2px(22)}')
		path_points.append(f'L{path_init_pos[0]},{group_y[1]-mm2px(float(box_connector[0]))}')
	
		#EXPLODE POLY POINTS ARRAY INTO STRING 
		path_string = " "
		path_string = path_string.join(path_points)  

		#GROUP POLYLINE GROUP 4
		svg_code += f'<path d="{path_string}" stroke="#00aeef" fill="none" stroke-width="2"/>'  

		###GROUP 5
		#SET PATHLINE INITAL POSITION FOR EASY USE ON CALCULATION OF OTHER POINTS
		path_init_pos = [float(group_x[0])+mm2px(float(flap_9[0])), {group_y[1]}]
	
		#ARRAY WITH [TOP Y POSITION, BOTTOM Y POSITION] AND [LEFT X POSITION, RIGHT X POSITION] 
		group_y = [group_y[1], group_y[1]+mm_to_pixels(group_5[1])]
		group_x = get_left_and_right_position(group_5, page_width)
	
		#GROUP FIVE DASHED LINES
		svg_code += f'<line x1="{float(group_x[0])+mm2px(float(flap_11[0]))}" x2="{float(group_x[0])+mm2px(float(flap_11[0]))}" y1="{group_y[0]+mm2px(4)}" y2="{group_y[1]}" stroke="#00aeef" stroke-dasharray="15" stroke-width="2px"/>'
		svg_code += f'<line x1="{float(group_x[1])-mm2px(float(flap_12[0]))}" x2="{float(group_x[1])-mm2px(float(flap_12[0]))}" y1="{group_y[0]+mm2px(4)}" y2="{group_y[1]}" stroke="#00aeef" stroke-dasharray="15" stroke-width="2px"/>'
	
		#PATH LINE
		path_points = [f'M{path_init_pos[0]},{path_init_pos[1]}']
		path_points.append(f'{group_x[0]+mm2px(float(flap_11[0]))},{group_y[0]+mm2px(4)}')
		path_points.append(f'{group_x[0]+mm2px(10)},{group_y[0]+mm2px(4)}')
		path_points.append(f'Q{group_x[0]+mm2px(1)},{group_y[0]+mm2px(5)}')
		path_points.append(f'{group_x[0]},{group_y[0]+mm2px(14)}')
		path_points.append(f'Q{group_x[0]+mm2px(5)},{group_y[1]-mm2px(10)}')
		path_points.append(f'{group_x[0]+mm2px(float(flap_11[0])-4)},{group_y[1]-mm2px(4)}')
		path_points.append(f'L{group_x[0]+mm2px(float(flap_11[0]))},{group_y[1]}')
		path_points.append(f'H{float(group_x[1])-mm2px(float(flap_12[0]))}')
		path_points.append(f'L{(group_x[1]-mm2px(float(flap_12[0])))+mm2px(4)},{group_y[1]-mm2px(4)}')
		path_points.append(f'Q{group_x[1]-mm2px(5)},{group_y[1]-mm2px(10)}')
		path_points.append(f'{group_x[1]},{group_y[0]+mm2px(14)}')
		path_points.append(f'Q{group_x[1]-mm2px(1)},{group_y[0]+mm2px(5)}')
		path_points.append(f'{group_x[1]-mm2px(10)},{group_y[0]+mm2px(4)}')
		path_points.append(f'H{float(group_x[1])-mm2px(float(flap_12[0]))}')
		path_points.append(f'L{float(group_x[1])-mm2px(float(flap_12[0])+float(box_connector[0]))},{group_y[0]}')
	
		#EXPLODE POLY POINTS ARRAY INTO STRING 
		path_string = " "
		path_string = path_string.join(path_points)  

		#GROUP POLYLINE GROUP 5
		svg_code += f'<path d="{path_string}" stroke="#00aeef" fill="none" stroke-width="2"/>'  

		#FOOTER
		pos_x = get_initial_pos_x(page_width-(page_margin*2), page_width)
		pos_y = mm_to_pixels(page_lenght-100)
		
		svg_code += get_footer(pos_x, pos_y, page_width, page_lenght, base_name,version, page_margin)
		
		svg_code += f'</svg>' 
		
		return svg_code   
		
  