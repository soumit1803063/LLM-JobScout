# job_extraction.py
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import streamlit as st

def get_prompt_template():
    """
    Returns a refined prompt template for accurate job data extraction.
    """
    return PromptTemplate.from_template("""
    ### SCRAPED TEXT FROM JOB WEBSITE:
    {page_content}

    ### INSTRUCTION:
    Analyze the text to identify job postings specifically related to Computer Science & Engineering (CSE). 
    Organize each posting into a structured JSON format with the following details:
    - `type`: The type/category of the job (e.g., Full-time, Part-time, Internship, etc.)
    - `role`: The specific role or title of the job
    - `Company`: Name of the company where the job is.
    - `experience`: Required experience level (e.g., Entry-level, Mid-level, Senior, etc.)
    - `skills`: Key skills or qualifications needed for the role
    - `deadline`: The application deadline, if available
    - `application_process`: Instructions on how to apply
    - `description`: Brief description of the role and responsibilities

    Only return a JSON array of objects with valid job data, without preamble or extraneous information.
    """)

def extract_job_data(llm, prompt, webpage_content):
    """
    Extracts and parses job data using the LLM model and prompt template.
    """
    chain = prompt | llm
    response = chain.invoke(input={"page_content": webpage_content})
    
    # Parse the response into JSON
    json_parser = JsonOutputParser()
    try:
        job_data = json_parser.parse(response.content)
    except ValueError:
        job_data = None
        st.error("Parsing error: Unable to extract valid JSON data.")
    
    return job_data
