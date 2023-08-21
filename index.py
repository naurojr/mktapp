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