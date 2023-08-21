import time
import include.simplemath
import include.convert


def get_footer(pos_x, pos_y, page_width, page_lenght, base_name,version, page_margin,file_type='dieline'): 
  
  #global version, page_margin
  
  localtime = time.strftime('%x at %X')
  
  #NAME SHORTENING FOR IMPORTED FUNCTIONS
  mm2px = include.convert.mm2px
  mm_to_pixels = include.convert.mm_to_pixels
  get_initial_pos_x = include.convert.get_initial_pos_x
  set_to_center = include.convert.set_to_center
  
  
  
  atom_box = set_to_center((page_width-(page_margin*2)), 80, pos_x, pos_y) 
  
  #return f'Page Width {page_width} page_margin {page_margin} atom_box {atom_box[2]}'
   
  svg_code = f'<rect x="{mm2px(page_margin)}" y="{atom_box[1]}" width="{mm_to_pixels(atom_box[2])}" height="{mm_to_pixels(atom_box[3])}" stroke="#000000" fill="none" stroke-width="1px"/>'
  svg_code += f'<text x="{mm_to_pixels(40)}" y="{pos_y+50}" fill="#000000" font-size="28" font-family="Arial, Helvetica, sans-serif">PAGE SIZE: {float(page_width)}mm X {float(page_lenght)}mm - SKU: {base_name}</text>'
  svg_code += f'<text x="{mm_to_pixels(40)}" y="{pos_y+80}" fill="#000000" font-size="18" font-weight="bold" font-family="Arial, Helvetica, sans-serif">©2019 The Rebel Idea, Inc. All Rights Reserved </text>'
  svg_code += f'<text x="{mm_to_pixels(40)}" y="{pos_y+120}" fill="#000000" font-size="20" font-family="Arial, Helvetica, sans-serif">CREATION DATE: {localtime}</text>'    
  
  
  svg_code += f'<g x="{mm_to_pixels(40)}" y="{pos_y+150}" transform="translate({mm_to_pixels(40)} {pos_y+138}) scale(1)">'
  svg_code +='''<g>
				<g>
				<path d="m76.3 22l6.1 35h-4l-1.4-7.7-6 3.1-0.7 4.6h-4l5.9-35h4.1zm-4.7 26.5l4.9-2.7-2.2-14.8-2.7 17.5z"/>
				<path d="m89.2 20.6v36.4h-4v-35.5l4-0.9z"/>
				<path d="m97.3 20.6v36.4h-4v-35.5l4-0.9z"/>
				<path d="m112.2 22v4h-3.9v31h-4.1v-31h-3.9v-4h11.9z"/>
				<path d="m126.3 50.7c0 1-0.2 2-0.5 2.8-0.4 0.8-0.8 1.5-1.5 2.1-0.6 0.6-1.3 1-2.2 1.3-0.8 0.3-1.7 0.4-2.6 0.4-1 0-1.8-0.2-2.7-0.4-0.8-0.3-1.5-0.7-2.1-1.3s-1.1-1.3-1.5-2.1-0.5-1.7-0.5-2.8v-14.8c0-1 0.2-1.9 0.5-2.7 0.4-0.8 0.8-1.5 1.5-2.1 0.6-0.6 1.3-1 2.1-1.3s1.7-0.4 2.7-0.4c0.9 0 1.8 0.2 2.6 0.4 0.8 0.3 1.6 0.7 2.2 1.3s1.1 1.3 1.5 2.1 0.5 1.7 0.5 2.7v14.8zm-9.8-0.2c0 1 0.3 1.7 0.8 2.2 0.6 0.5 1.3 0.7 2.1 0.7s1.6-0.2 2.1-0.7 0.8-1.2 0.8-2.2v-14.4c0-1-0.3-1.7-0.8-2.2s-1.2-0.7-2.1-0.7-1.6 0.2-2.1 0.7c-0.6 0.5-0.8 1.2-0.8 2.2v14.4z"/>
				<path d="m132.9 29.7l0.6 1.5c1.4-1.3 3-1.9 4.7-1.9 0.9 0 1.8 0.2 2.5 0.6 0.8 0.4 1.4 1 1.9 1.8 0.7-0.8 1.5-1.4 2.4-1.8s1.8-0.6 2.8-0.6c0.7 0 1.5 0.1 2.1 0.4 0.7 0.3 1.3 0.7 1.8 1.2 0.5 0.6 0.9 1.2 1.2 2.1 0.3 0.8 0.4 1.8 0.4 2.9v21h-4v-20.1c0-1.1-0.2-2-0.6-2.6s-1.1-0.9-2.1-0.9c-1.1 0-2.1 0.5-3 1.4 0 0.2 0.1 0.4 0.1 0.6v0.6 21h-4v-20.1c0-1.1-0.2-2-0.6-2.6s-1.1-0.9-2.1-0.9c-1.1 0-2.1 0.4-2.9 1.3v22.4h-4v-27.3h2.8z"/>
				<path d="m157.8 32.4c0.7-1 1.5-1.7 2.7-2.2s2.4-0.8 3.7-0.8c2.2 0 3.8 0.7 4.9 2.1s1.6 3.2 1.6 5.3v20.2h-2.5l-0.7-1.5c-0.7 0.6-1.5 1-2.3 1.4-0.8 0.3-1.8 0.5-2.7 0.5-0.7 0-1.5-0.1-2.2-0.4s-1.3-0.7-1.9-1.2c-0.5-0.6-1-1.3-1.3-2.2s-0.5-2-0.5-3.3c0-1 0.1-1.9 0.3-2.8 0.2-0.8 0.5-1.6 1-2.4 0.5-0.7 1-1.5 1.8-2.2 0.7-0.7 1.6-1.4 2.5-2.2l2.1-1.5c0.8-0.5 1.6-1.1 2.5-1.6v-0.8c0-1.1-0.3-2.1-0.8-2.8s-1.4-1.1-2.5-1.1c-0.8 0-1.5 0.2-2.1 0.6s-1.1 0.9-1.5 1.5l-2.1-2.6zm5.7 21.2c0.6 0 1.2-0.1 1.7-0.4s1.1-0.7 1.6-1.2v-10.5c-0.5 0.3-1 0.6-1.4 0.9l-1.2 0.9c-1.4 1.1-2.4 2.2-2.9 3.2s-0.8 2.1-0.8 3.2c0 1.4 0.3 2.4 0.8 3 0.6 0.6 1.3 0.9 2.2 0.9z"/>
				<path d="m176 29.7v-4.8l3.8-1.6v6.4h4.6v3.3h-4.6v17.2c0 1 0.3 1.9 0.8 2.4 0.5 0.6 1.2 0.9 2.1 0.9 0.7 0 1.4-0.2 2-0.7l1.1 3.4c-0.5 0.4-1.1 0.6-1.7 0.8s-1.3 0.3-2 0.3c-1.1 0-2-0.2-2.8-0.6s-1.4-0.9-1.9-1.5-0.9-1.4-1.1-2.3-0.4-1.8-0.4-2.7v-17.2h-2.9v-3.3h3z"/>
				<path d="m201.7 50.7c0 1-0.2 2-0.5 2.8-0.4 0.8-0.8 1.5-1.5 2.1-0.6 0.6-1.3 1-2.2 1.3-0.8 0.3-1.7 0.4-2.6 0.4-1 0-1.8-0.2-2.7-0.4-0.8-0.3-1.5-0.7-2.1-1.3s-1.1-1.3-1.5-2.1-0.5-1.7-0.5-2.8v-14.8c0-1 0.2-1.9 0.5-2.7 0.4-0.8 0.8-1.5 1.5-2.1 0.6-0.6 1.3-1 2.1-1.3s1.7-0.4 2.7-0.4c0.9 0 1.8 0.2 2.6 0.4 0.8 0.3 1.6 0.7 2.2 1.3s1.1 1.3 1.5 2.1 0.5 1.7 0.5 2.7v14.8zm-9.7-0.2c0 1 0.3 1.7 0.8 2.2 0.6 0.5 1.3 0.7 2.1 0.7 0.9 0 1.6-0.2 2.1-0.7s0.8-1.2 0.8-2.2v-14.4c0-1-0.3-1.7-0.8-2.2s-1.2-0.7-2.1-0.7-1.6 0.2-2.1 0.7c-0.6 0.5-0.8 1.2-0.8 2.2v14.4z"/>
				<path d="m215.9 34c-0.8-0.5-1.7-0.8-2.5-0.8-1.5 0-2.8 0.8-3.8 2.3v21.5h-4v-27.3h2.7l0.8 2.3c1.2-1.8 2.7-2.6 4.6-2.6 0.6 0 1.2 0.1 1.7 0.3 0.6 0.2 1.1 0.5 1.6 0.9l-1.1 3.4z"/>
				</g>
				<g>
				<path d="m22 37v-22.3h-2.2c-1.3 0-2.5 1-2.7 2.3l-0.5 3.9c-1 0.3-1.9 0.6-2.8 1l-3-2.3c-1.1-0.8-2.6-0.7-3.5 0.2l-2.1 2.2c-1 1-1 2.5-0.2 3.5l2.2 2.8c-0.5 1-1 2-1.3 3.1l-3.4 0.4c-1.5 0.2-2.5 1.3-2.5 2.6v3c0 1.3 1 2.5 2.3 2.7l3.4 0.4c0.3 1.1 0.8 2.1 1.3 3.1l-2.2 2.8c-0.8 1.1-0.7 2.6 0.2 3.5l2.3 2.1c1 1 2.5 1 3.5 0.2l3-2.3c0.9 0.4 1.8 0.8 2.8 1l0.5 3.9c0.2 1.3 1.3 2.3 2.7 2.3h2.2v-20.1z" fill="#C1272D"/>
				<path d="m21.1 37v-22.3h1.5c1.3 0 2.5 1 2.7 2.3l0.5 3.9c1 0.3 1.9 0.6 2.8 1l3-2.3c1.1-0.8 2.6-0.7 3.5 0.2l2.1 2.1c1 1 1 2.5 0.2 3.5l-2.2 2.8c0.5 1 1 2 1.3 3.1l3.4 0.4c1.3 0.2 2.3 1.3 2.3 2.7v3c0 1.3-1 2.5-2.3 2.7l-3.4 0.4c-0.3 1.1-0.8 2.1-1.3 3.1l2.2 2.8c0.8 1.1 0.7 2.6-0.2 3.5l-2.2 2.1c-1 1-2.5 1-3.5 0.2l-3-2.3c-0.9 0.4-1.8 0.8-2.8 1l-0.5 3.9c-0.2 1.3-1.3 2.3-2.7 2.3h-1.5v-20.1z" fill="#4D4D4E"/>
				<g>
				<path d="m52.4 33.5h-2.3c-1.3 0-2.4-1-2.6-2.3l-0.3-2.6c-0.5-0.2-1-0.3-1.5-0.6l-2 1.5c-1 0.8-2.5 0.7-3.5-0.2l-1.6-1.6c-0.9-0.9-1-2.4-0.2-3.5l1.4-1.8c-0.3-0.6-0.5-1.1-0.7-1.7l-2.2-0.3c-1.3-0.2-2.3-1.3-2.3-2.6v-2.3c0-1.3 1-2.4 2.3-2.6l2.2-0.3c0.2-0.6 0.5-1.2 0.7-1.7l-1.4-1.8c-0.8-1-0.7-2.5 0.2-3.5l1.6-1.6c0.9-0.9 2.4-1 3.5-0.2l2 1.5 1.5-0.6 0.3-2.6c0.1-1.1 1.3-2.1 2.6-2.1h2.3c1.3 0 2.4 1 2.6 2.3l0.4 2.9c0.4 0.2 0.8 0.3 1.1 0.5l2.3-1.8c1-0.8 2.5-0.7 3.5 0.2l1.6 1.6c0.9 0.9 1 2.4 0.2 3.5l-2 2.5c0.1 0.3 0.2 0.6 0.4 0.9l3.2 0.4c1.3 0.2 2.3 1.3 2.3 2.6v2.3c0 1.3-1 2.4-2.3 2.6l-3.2 0.4c-0.1 0.3-0.2 0.6-0.4 0.9l2 2.5c0.8 1 0.7 2.5-0.2 3.5l-1.6 1.6c-0.9 0.9-2.4 1-3.5 0.2l-2.3-1.8c-0.3 0.2-0.7 0.3-1.1 0.5l-0.4 2.9c-0.2 1.3-1.3 2.3-2.6 2.3zm-6.9-6.8l0.3 0.2c0.6 0.3 1.3 0.6 2 0.8l0.4 0.1 0.4 3.4c0.1 0.7 0.7 1.3 1.4 1.3h2.3c0.7 0 1.3-0.5 1.4-1.3l0.5-3.6 0.3-0.1c0.6-0.2 1.1-0.5 1.6-0.7l0.3-0.2 3 2.3c0.6 0.4 1.4 0.4 1.9-0.1l1.7-1.8c0.5-0.5 0.6-1.3 0.1-1.9l-2.4-3.1 0.2-0.3c0.2-0.5 0.4-1 0.6-1.4l0.1-0.4 4-0.5c0.7-0.1 1.3-0.7 1.3-1.4v-2.3c0-0.7-0.5-1.3-1.3-1.4l-4-0.5-0.1-0.4c-0.1-0.4-0.3-0.9-0.6-1.4l-0.2-0.3 2.4-3.1c0.4-0.6 0.4-1.4-0.1-1.9l-1.6-1.7c-0.5-0.5-1.3-0.6-1.9-0.1l-3 2.3-0.3-0.2c-0.5-0.3-1-0.5-1.6-0.7l-0.3-0.1-0.5-3.6c-0.1-0.7-0.7-1.3-1.4-1.3h-2.3c-0.7 0-1.3 0.5-1.4 1.3l-0.4 3.4-0.4 0.1c-0.7 0.2-1.4 0.4-2 0.8l-0.3 0.2-2.6-2c-0.6-0.7-1.5-0.7-2-0.1l-1.6 1.6c-0.5 0.5-0.6 1.3-0.1 1.9l1.9 2.4-0.2 0.3c-0.4 0.7-0.7 1.5-1 2.2l-0.1 0.4-3 0.4c-0.7 0.1-1.3 0.7-1.3 1.4v2.3c0 0.7 0.5 1.3 1.3 1.4l3 0.4 0.1 0.4c0.2 0.7 0.6 1.5 1 2.2l0.2 0.3-1.9 2.4c-0.4 0.6-0.4 1.4 0.1 1.9l1.6 1.6c0.5 0.5 1.3 0.6 1.9 0.1l2.6-1.9z"/>
				</g>
				</g>
				</g>
				<g fill="#010101">
				<path d="m131.5 2.7h2.5l3.7 10.9 3.7-10.9h2.5v12.9h-1.7v-7.6-1.3s0-1.3 0-2l-3.7 10.9h-1.7l-3.7-10.9v0.4 1.4 1.4 7.6h-1.7v-12.8z"/>
				<path d="m151.3 9.9c0.4 0 0.6-0.2 0.7-0.5 0.1-0.1 0.1-0.3 0.1-0.6 0-0.5-0.2-0.9-0.6-1.2-0.4-0.2-0.9-0.4-1.6-0.4-0.8 0-1.4 0.2-1.7 0.7-0.2 0.2-0.3 0.6-0.4 1.1h-1.5c0-1.2 0.4-2 1.1-2.4 0.7-0.5 1.6-0.7 2.5-0.7 1.1 0 2 0.2 2.7 0.6s1 1.1 1 2v5.4c0 0.2 0 0.3 0.1 0.4s0.2 0.1 0.4 0.1h0.2 0.3v1.2c-0.2 0.1-0.4 0.1-0.6 0.1h-0.5c-0.5 0-0.9-0.2-1.2-0.6-0.1-0.2-0.2-0.5-0.3-0.9-0.3 0.4-0.8 0.8-1.4 1.1s-1.3 0.5-2 0.5c-0.9 0-1.6-0.3-2.1-0.8-0.6-0.5-0.8-1.2-0.8-2 0-0.9 0.3-1.5 0.8-2s1.3-0.8 2.1-0.9l2.7-0.2zm-3.3 4.2c0.3 0.3 0.7 0.4 1.2 0.4 0.6 0 1.1-0.1 1.6-0.4 0.9-0.4 1.3-1.1 1.3-2.1v-1.3c-0.2 0.1-0.4 0.2-0.7 0.3s-0.6 0.1-0.9 0.2l-1 0.1c-0.6 0.1-1 0.2-1.3 0.4-0.5 0.3-0.7 0.7-0.7 1.3 0 0.5 0.1 0.9 0.5 1.1z"/>
				<path d="m161.4 6.5c0.3 0.2 0.6 0.5 1 0.9v-4.8h1.5v12.9h-1.4v-1.3c-0.4 0.6-0.8 1-1.3 1.3s-1.1 0.4-1.7 0.4c-1 0-1.9-0.4-2.7-1.3s-1.1-2.1-1.1-3.5 0.3-2.6 1-3.6 1.7-1.5 3-1.5c0.6 0 1.2 0.2 1.7 0.5zm-3.5 7c0.4 0.7 1.1 1 2 1 0.7 0 1.3-0.3 1.8-0.9s0.7-1.5 0.7-2.7-0.2-2.1-0.7-2.6c-0.5-0.6-1.1-0.9-1.8-0.9-0.8 0-1.4 0.3-1.9 0.9s-0.7 1.5-0.7 2.7c0 1 0.2 1.8 0.6 2.5z"/>
				<path d="m172 6.4c0.6 0.3 1.1 0.7 1.4 1.2s0.5 1 0.6 1.7c0.1 0.4 0.1 1.1 0.1 2.1h-6.8c0 1 0.3 1.7 0.7 2.3s1.1 0.9 1.9 0.9 1.5-0.3 2-0.8c0.3-0.3 0.5-0.7 0.6-1.1h1.6c0 0.3-0.2 0.7-0.4 1.2-0.2 0.4-0.5 0.8-0.8 1-0.5 0.5-1.1 0.8-1.8 0.9-0.4 0.1-0.8 0.1-1.3 0.1-1.2 0-2.1-0.4-3-1.3-0.8-0.8-1.2-2-1.2-3.6 0-1.5 0.4-2.7 1.2-3.7 0.8-0.9 1.9-1.4 3.2-1.4 0.8 0.1 1.4 0.2 2 0.5zm0.6 3.7c-0.1-0.7-0.2-1.2-0.4-1.6-0.4-0.8-1.1-1.1-2.1-1.1-0.7 0-1.3 0.3-1.8 0.8s-0.7 1.2-0.8 2h5.1z"/>
				<path d="m181.9 6.2l1.8 7.4 1.8-7.4h1.8l1.8 7.4 1.9-7.4h1.6l-2.7 9.4h-1.6l-1.9-7.3-1.8 7.3h-1.6l-2.7-9.4h1.6z"/>
				<path d="m194.2 2.7h1.6v1.8h-1.6v-1.8zm0 3.5h1.6v9.3h-1.6v-9.3z"/>
				<path d="m198.5 3.5h1.6v2.6h1.5v1.3h-1.5v6.1c0 0.3 0.1 0.5 0.3 0.7 0.1 0.1 0.3 0.1 0.6 0.1h0.2 0.3v1.3c-0.2 0.1-0.4 0.1-0.6 0.1h-0.6c-0.7 0-1.2-0.2-1.5-0.6s-0.4-0.9-0.4-1.5v-6.1h-1.3v-1.3h1.3v-2.7z"/>
				<path d="m203.1 2.6h1.6v4.8c0.4-0.5 0.7-0.8 1-1 0.5-0.3 1.1-0.5 1.9-0.5 1.4 0 2.3 0.5 2.8 1.4 0.3 0.5 0.4 1.2 0.4 2.2v6h-1.6v-5.9c0-0.7-0.1-1.2-0.3-1.5-0.3-0.5-0.8-0.8-1.6-0.8-0.7 0-1.2 0.2-1.8 0.7s-0.8 1.3-0.8 2.6v5h-1.6v-13z"/>
				</g>'''
  svg_code += f'<text transform="translate(133.97 77.793)" fill="#000000" font-family="Helvetica" font-size="14.514px">version {version}</text></g>'
  
  return svg_code