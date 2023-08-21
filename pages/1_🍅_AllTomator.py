import streamlit as st

import math, time, os
import pandas as pd
import json, base64

import os.path
import pathlib

import include.simplemath
import include.convert

from include import DielineClass
from include import SafezoneClass
from include import GetFooter

from io import StringIO
from pathlib import Path
import shutil

# Use the xlwt module as the Excel writer.
import xlwt

from reportlab.graphics import renderPDF, renderPM
from svglib.svglib import svg2rlg

#BARCODE GENERATOR
from barcode import UPCA

# USED TO CALCULATE PRECISION DIVISION
from decimal import *

#SET TIMEZONE
os.environ['TZ'] = 'US/Eastern'
time.tzset()

version = "1"
tomato = {}

# Get the current working directory
current_directory = os.getcwd()


#PROMPT FINDER TO FIND THE FILE
intake_sheet = ""

#NAME CASTING FOR IMPORTED FUNCTIONS
mm2px = include.convert.mm2px
mm_to_pixels = include.convert.mm_to_pixels
get_initial_pos_x = include.convert.get_initial_pos_x


st.set_page_config(
	page_title="AllTomator",
	page_icon=":tomato:",
)

st.title("AllTomator :tomato:", anchor=None)

if "authentication_status" not in st.session_state or st.session_state["authentication_status"] is None: 
	st.error('Login to use this tool', icon="🚨")
else: 
	
	"Upload a CSV file and AllTomator will create the packaging assets for you. It's easy as smashing a tomato."
	uploaded = st.file_uploader("Choose a CSV file", type=['csv'])
	
	#https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader
	if uploaded is not None:
		# To read file as bytes:
		bytes_data = uploaded.getvalue()
		#st.write(bytes_data)
								
		# To convert to a string based IO:
		stringio = StringIO(uploaded.getvalue().decode("utf-8"))
		#st.write(stringio)
								
		# To read file as string:
		string_data = stringio.read()
		#st.write(string_data)
								
		# Can be used wherever a "file-like" object is accepted:
		# Import the excel data and convert long numbers (BARCODE AND ITEM NUMBER) to string 
		df_intake = pd.read_csv(uploaded, converters={'ITEM_CODE':str, 'SKU':str, 'EACH_BARCODE':str, 'BOX_BARCODE':str})
		st.write(df_intake)	
		
		# Set display precision to remove exponential notation on barcodes
		pd.set_option('display.precision',9)
		
		#SET ORIGINAL PATH ON COLAB
		#IT SHOULD BE DINAMYC WHEN CONVERTED TO GUI
		path = '/content'
		unit_of_measurement = "mm"
		cardboard_thickness = 5.8
		is_piece_measurement = True 
		
		#LOOP ON THE FILE AND MAKE THE BOX
		for index, item in df_intake.iterrows():
		
			if not pd.isna(item[0]):
		    	#GET DATA FROM INTAKE_SHEET
				sku = str(item.loc['SKU'])
				item_code = str(item.loc['ITEM_CODE'])
				brand = str(item.loc['BRAND'])
				mosaic_width = int(item.loc['PC_OVERALL_WIDTH_MM'])
				mosaic_length = int(item.loc['PC_OVERALL_LENGTH_MM'])    
				mosaic_height = int(item.loc['PC_MAX_THICKNESS_MM'])
				pieces_per_box = int(item.loc['PCS_PER_BOX'])
				need_backercard = bool(item.loc['NEED_BACKER_CARD'])
				window = bool(item.loc['BOX_HAS_WINDOW'])
				each_upc = int(item.loc['EACH_BARCODE'])
				box_upc = int(item.loc['BOX_BARCODE'])
				base_name = item_code.strip()
				
				#SET FOLD DIMENSION CONSTANT
				box_connector = [cardboard_thickness, (mosaic_length+9)*0.14]
				fold_1 = fold_2 = float(box_connector[0])
				
				#BACKERCARD DIMENSIONS
				backercard_lenght = mosaic_length+2
				backercard_width = mosaic_width+2
				
				#SET WINDOW SIZE IN MM
				window_size = 127
				
				#BOX HEIGHT
				if need_backercard:
					box_height = (mosaic_height+2)*pieces_per_box
				else:
					box_height = (mosaic_height*pieces_per_box)+2	
				
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
				
				#SET MARGIN
				page_margin = 30
				page_margin_bottom = 180
				
				#CALCULATE PAGE DIMENSIONS IN MM
				page_width = math.ceil(float(float(group_2[0])+(page_margin*2)))
				page_lenght = math.ceil(float(group_1[1])+float(group_2[1])+float(group_3[1])+float(group_4[1])+float(group_5[1])+page_margin+page_margin_bottom)
				
				#ADD PAGE SIZE TO TOMATO FILE
				tomato["file_name"] = f'{base_name}'
				tomato["item_data"] = {}
				tomato["item_data"]['sku'] = f'{sku}'
				tomato["item_data"]['item_code'] = f'{item_code}'
				tomato["document_size"] = {'width':page_width,'length':page_lenght,'unit':'mm'}
				
				#CONVERT PAGE DIMENSIONS TO PIXEL
				page_width_in_pixels = mm_to_pixels(page_width);
				page_lenght_in_pixels = mm_to_pixels(page_lenght);
				
				#SET INITIAL POSITION FOR PLACEMENT OF THE ELEMENTS
				pos_x = get_initial_pos_x(group_1[0], page_width)
				pos_y = mm_to_pixels(page_margin)
				
				#CREATE FOLDER PATH
				folder_path = os.path.join(current_directory, f'content/{base_name}')
				
				#DELETE FOLDER WITH THE SKU NAME, IF EXISTS
				#!rm -rf '{base_name}'
				shutil.rmtree(folder_path)
				
				#MAKE EMPTY FOLDER WITH SKU NAME
				#!mkdir '{base_name}'
				# Join the current directory path with the folder name
				os.makedirs(folder_path)
			
				#CREATE SVG FILENAME
				dieline_filename = f'{base_name}_DL.svg'
				safezone_filename = f'{base_name}_SZ.svg'
				backercard_filename = f'{base_name}_BC.svg'  			 
				
				#CREATE DIELINE SVG
				dieline = include.DielineClass.Dieline()
				dl_code = dieline.getDielineSVG(backercard_width, backercard_lenght, box_connector, box_height, page_width, page_lenght, page_margin, page_margin_bottom, window, version, sku, base_name, fold_1, fold_2)

				#SAVE DIELINE TO SVG 
				f = open(f'{folder_path}/{dieline_filename}', "w+")
				f.write(dl_code)
				f.close()

				#SAVE DIELINE TO PDF
				dielinefile = svg2rlg(f'{folder_path}/{dieline_filename}')
				renderPDF.drawToFile(dielinefile, f'{folder_path}/{base_name}_DL.pdf')
				
				tomato['files'] = {}
				tomato['files']['dieline'] = f'{base_name}_DL.pdf'
				tomato['files']['safezone'] = safezone_filename
	
				#CREATE SAFEZONE SVG
				safezone = include.SafezoneClass.SafeZone()
				safezone_svg_code = safezone.getSafeZoneSVG(backercard_width, backercard_lenght, box_connector, box_height, page_width, page_lenght, page_margin, page_margin_bottom, fold_1, fold_2)
				
				#SAVE SAFEZONE TO FILE
				f = open(f'{folder_path}/{safezone_filename}', "w+")
				f.write(safezone_svg_code)
				f.close()

				#CREATE BACKERCARD IF REQUESTED
				if need_backercard:
					backercard = BackerCard(backercard_width, backercard_lenght)
					backercard_svg_code = backercard.getBackerCardSVG()
				
					#SAVE BACKERCARD TO FILE
					f = open(backercard_filename, "w+")
					f.write(backercard_svg_code)
					f.close()
					
					#SAVE BACKERCARD TO PDF
					backercardfile = svg2rlg(backercard_filename)
					renderPDF.drawToFile(backercardfile, f'{base_name}_BC.pdf') 
					#!rm -r '{base_name}_BC.svg'				
				
	
	#normalize name form imported funciton to local
	normalize_number = include.simplemath.normalize_number
	myNum = normalize_number(09.151445,1)
	f'{myNum}'


	f'{mm2px(1)}'	
	
	tomato
	current_directory
