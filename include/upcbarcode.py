import os

from barcode import generate
from reportlab.graphics import renderPDF, renderPM
from svglib.svglib import svg2rlg

def create_upc_barcode(upc_string):
	box_barcode = generate('UPCA',upc_string, output=upc_string)
	
	f = open(box_barcode, "r+")
	svg_content = f.read()
	svg_content = svg_content.replace('height="15.000mm"', 'height="11.000mm"')
	svg_content = svg_content.replace('y="21.000mm"', 'y="16.000mm"')
	svg_content = svg_content.replace('height="23.000mm"', 'height="20.000mm"')
	f.seek(0)
	f.write(svg_content)
	f.truncate()
	f.close()
	
	backercardfile = svg2rlg(f'{box_barcode}')
	renderPDF.drawToFile(backercardfile, f'{box_barcode[:-4]}.pdf') 
	#rm box_barcode
	os.remove(f'{box_barcode}')
    
	return True