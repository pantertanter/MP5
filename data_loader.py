import streamlit as st
from docx import Document


# ------------------functions to load documents----------------

def load_docx(path):
    return Document(path)

# Load the DOCX document
doc = load_docx("./data/BarackHusseinObamaWiki.docx")

# Extract text from paragraphs and join them into a single string
doc_text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])

# Display the text in a Streamlit text area
st.text_area("Document Content", value=doc_text, height=400)

def load_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# ------------------function to make a dict 1 means the word accours----------------

# Binary vector of word appearance in a sentence
def vect(sent, corpus):
    # create new dict and place zeros in it
    mydict = dict.fromkeys(corpus, 0) 
    
    # code each word's appearance in the sentence with 1
    for word in sent:
        mydict[word] = 1
    return mydict    



