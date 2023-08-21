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

st.title("Marketing Tools :toolbox:", anchor=None)