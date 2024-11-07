# config.py
import os
from dotenv import load_dotenv
import streamlit as st
# Load environment variables
# load_dotenv()
GROQ_API_KEY = st.secrets['GROQ_API_KEY']#os.getenv('GROQ_API_KEY')
