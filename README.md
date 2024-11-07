# LLM JobScout

LLM JobScout is an advanced web application designed to streamline the extraction and organization of Computer Science & Engineering (CSE) job listings from online job portals. Utilizing a large language model (LLM) via the Groq API and LangChain, the app scrapes job-related content from specified websites and organizes it into a structured JSON format. This enables job seekers and data analysts to easily view and analyze CSE-specific job postings, sorted by role, experience, required skills, deadline, and more.

## Live App Link
[LLM Job Scout](https://llm-jobscout-h2agdm9r2bspabr8ssguy9.streamlit.app/)


## Demo

Watch a demonstration of **LLM JobScout** in action:

[![LLM JobScout Demo](https://img.youtube.com/vi/edVdWXfbX64/0.jpg)](https://youtu.be/edVdWXfbX64)


## Key Features
- **Targeted Job Data Extraction**: Extracts and structures CSE job postings based on role, experience, required skills, deadline, and other key information.
- **Modular and Scalable Architecture**: Built with Streamlit and LangChain to ensure scalability and modularity for easy extension and maintenance.
- **User-Friendly Interface**: Allows users to input a job website URL and retrieve job postings in a clean, organized JSON format.
- **Efficient and Fast Processing**: Uses Groq's powerful infrastructure to ensure high performance and accuracy in data extraction.

## Technology Stack

### Large Language Model (LLM) - Llama3-8b-8192
We have integrated **Llama3-8b-8192**, a state-of-the-art language model optimized for natural language understanding. Llama3 excels at parsing unstructured text, allowing it to accurately identify and categorize CSE-specific job listings from the raw content of job websites. By using this model, we ensure that job data is extracted with high precision, regardless of the complexity of the job descriptions.

### Groq API
We utilize the **Groq API** for running the Llama3-8b-8192 model. Groq's infrastructure provides highly efficient, high-performance execution for large models, enabling fast and scalable processing of job-related content. This ensures that LLM JobScout can handle a large number of job listings from multiple sources, maintaining speed and accuracy without compromising performance.

### LangChain
**LangChain** is used to facilitate the orchestration of the LLM model and the extraction logic. With LangChain, we can create a modular, flexible pipeline that chains together various steps of data processing, from scraping the web content to formatting it into structured JSON. This modularity ensures the system can easily be extended or modified for future use cases.

## Installation

### Prerequisites
- Python 3.7 or later
- `pip` (Python package manager)

### Steps to Run Locally
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/LLM-JobScout.git
   cd LLM-JobScout
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Create a `.env` file in the root of the project and add your **Groq API key**:
   ```plaintext
   GROQ_API_KEY=your_api_key_here
   ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

## How to Use
1. Enter the URL of a job portal that lists CSE job postings.
2. Click on the **"Extract Job Data"** button.
3. The app will process the data, and you will see the extracted job listings displayed in a clean, organized JSON format.

## Project Structure
- **`app.py`**: Main Streamlit application file that handles user interactions and displays results.
- **`config.py`**: Contains environment-related configurations such as API keys.
- **`llm_utils.py`**: Handles initialization and management of the LLM model and API.
- **`job_extraction.py`**: Contains logic for extracting and formatting job postings using the LLM model.
- **`webpage_loader.py`**: Manages the loading and parsing of webpage content from specified URLs.

