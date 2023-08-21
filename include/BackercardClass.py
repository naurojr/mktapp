import os
import include.simplemath
import include.convert
import include.GetFooter

class BackerCard:
	
	def __init__(self, width, lenght, page_margin, page_margin_bottom):
	  
	  global page_margin, page_margin_bottom
	  
	  self.width = width
	  self.lenght = lenght
	  self.margin = page_margin
	  self.footer = page_margin_bottom
	
	def getBackerCardSVG(self): 
	
		page_width = math.ceil(float(float(self.width)+(self.margin*2)))
		page_lenght = math.ceil(float(float(self.lenght)+self.margin+self.footer))
		
		page_width_in_pixels = mm2px(page_width)
		page_lenght_in_pixels = mm2px(page_lenght)
 	
		#SET INITIAL POSITION FOR PLACEMENT OF THE ELEMENTS
		pos_x = get_initial_pos_x(self.width, page_width)
		pos_y = mm_to_pixels(page_margin)
			
		#WRITE SVG BASE CODE
		svg_code = f'<svg width="{page_width_in_pixels}" height="{page_lenght_in_pixels}" viewBox="0 0 {page_width_in_pixels} {page_lenght_in_pixels}">'  
   	
		#PANEL_ONE
		backer_card = set_to_center(self.width, self.lenght, pos_x, pos_y)    
		svg_code += f'<rect x="{backer_card[0]}" y="{backer_card[1]}" width="{mm_to_pixels(backer_card[2])}" height="{mm_to_pixels(backer_card[3])}" stroke="#00aeef"  fill="none" stroke-width="2px"/>'
	
		#FOOTER
		pos_x = get_initial_pos_x(page_width-(self.margin*2))
		pos_y = mm_to_pixels(page_lenght-100)
		
	
		svg_code += get_footer(pos_x, pos_y, page_width, base_name)
	
		svg_code += f'</svg>'
  	
		return svg_code