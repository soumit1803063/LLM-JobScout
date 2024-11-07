# app.py
import streamlit as st
from config import GROQ_API_KEY
from llm_utils import initialize_llm
from job_extraction import get_prompt_template, extract_job_data
from webpage_loader import load_webpage_data

# Streamlit app setup
def display_interface():
    st.set_page_config(page_title="CSE Job Listings Extractor", layout="wide")
    st.title("CSE Job Listings Extractor")
    st.write("Enter a job website URL to extract CSE-related job listings.")

    # URL input field with enhanced styling
    url_input = st.text_input("Job Website URL", "https://example.com")

    if st.button("Extract Job Data"):
        with st.spinner("Loading and processing data..."):
            # Load model and prompt template
            llm = initialize_llm(GROQ_API_KEY)
            prompt_template = get_prompt_template()

            # Load and extract job data
            webpage_data = load_webpage_data(url_input)
            job_data = extract_job_data(llm, prompt_template, webpage_data)

            # Display the extracted data
            if job_data:
                st.success("Job data extracted successfully!")
                for job in job_data:
                    with st.expander(f"{job.get('role', 'Job Role')} - {job.get('type', 'Job Type')}"):
                        st.json(job)
            else:
                st.error("Failed to extract or format job data. Please check the URL and try again.")

if __name__ == "__main__":
    display_interface()
