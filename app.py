import streamlit as st
import spacy
from spacy import displacy

# Load your pre-trained SpaCy model
nlp = spacy.load("output/model-best")

def extract_info_from_resume(resume_text):
    doc = nlp(resume_text)
    education = []
    skills = []
    for ent in doc.ents:
        if ent.label_ == "Education":
            education.append(ent.text)
        elif ent.label_ == "Skills":
            skills.append(ent.text)
    return education, skills

st.title("Resume Parser")
st.write("Upload a resume to extract education and skills information.")

uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    if uploaded_file.type == "text/plain":
        # Read the text file directly
        resume_text = uploaded_file.read().decode("utf-8")
    elif uploaded_file.type == "application/pdf":
    # Assume text extraction is handled, e.g., via PyMuPDF for PDFs
        import fitz  # PyMuPDF
        doc = fitz.open(stream=uploaded_file.read(), filetype=".txt")
        resume_text = ""
        for page in doc:
            resume_text += page.get_text()

    # Print extracted text for debugging
    # st.subheader("Extracted Text")
    # st.write(resume_text)

    education, skills = extract_info_from_resume(resume_text)

    # Debugging: Print extracted entities
    # st.subheader("Extracted Entities (Debugging)")
    doc = nlp(resume_text)
    # entities = [(ent.text, ent.label_) for ent in doc.ents]
    # st.write(entities)

    st.header("Extracted Information")
    st.subheader("Education")
    st.write(education)
    st.subheader("Skills")
    st.write(skills)

    # Custom colors for entities
    colors = {"Education": "linear-gradient(90deg, #aa9cfc, #fc9ce7)", "Skills": "linear-gradient(90deg, #fce38a, #f38181)"}
    options = {"ents": ["Education", "Skills"], "colors": colors}
    
    st.header("Annotated Resume")
    html = displacy.render(doc, style="ent", options=options)
    
    # Custom CSS to reduce spacing
    st.write("""
    <style>
        .entity { line-height: 1.0; }
        .entities { line-height: 1.0; }
    </style>
    """, unsafe_allow_html=True)

    st.write(html, unsafe_allow_html=True)