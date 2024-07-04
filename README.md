# Resume Parser Streamlit App

This Streamlit app allows users to upload resumes in PDF, DOCX, or TXT formats. It uses a pre-trained SpaCy model to extract education and skills information from the resumes and displays the extracted information along with an annotated version of the resume.

## Features

- Upload resumes in PDF, DOCX, or TXT formats.
- Extract education and skills information using a SpaCy model.
- Display extracted education and skills information.
- Annotate and display the resume with custom colors for different entity types.

## Requirements

- Python 3.6+
- Streamlit
- SpaCy
- PyMuPDF (for PDF processing)
- python-docx (for DOCX processing)

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/resume-parser-streamlit.git
   cd resume-parser-streamlit
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install the required packages
   ```sh
   pip install -r requirements.txt
4. Ensure you have your SpaCy model installed:
   ```sh
   python -m spacy download en_core_web_sm
5. Replace "path/to/your/spacy/model" in the code with the path to your SpaCy model.

## Usage
1. Run the Streamlit app:
    ```sh
    streamlit run app.py
2. Open your web browser and go to http://localhost:8501.
3. Upload a resume file in PDF, DOCX, or TXT format.
4. View the extracted education and skills information along with the annotated resume.
