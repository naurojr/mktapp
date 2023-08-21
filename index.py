import streamlit as st
import streamlit_authenticator as stauth
import os.path
import pathlib
import pandas as pd

from io import StringIO
from pathlib import Path


import yaml
from yaml.loader import SafeLoader

st.set_page_config(
	page_title="Mosaic Companies Marketing Tools",
	page_icon=":toolbox:",
)

with open('./config.yaml') as file:
	config = yaml.load(file, Loader=SafeLoader)

st.title("Marketing Tools :toolbox:", anchor=None)

authenticator = stauth.Authenticate(
		config['credentials'],
		config['cookie']['name'],
		config['cookie']['key'],
		config['cookie']['expiry_days'],
		config['preauthorized']
	)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
	authenticator.logout('Logout', 'main', key='unique_key')
	st.write(f'Welcome *{name}*')

	uploaded_file = st.file_uploader("Choose a CSV file", type=['xlsx','csv'])

elif authentication_status is False:
	st.error('Username/password is incorrect')
elif authentication_status is None:
	st.warning('Please enter your username and password')