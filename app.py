import streamlit as st
from data_loader import (load_docx, load_text_file,
                         vect)
import pandas as pd
from cosimfunc import cosim


# Load the data---------------------------------------

doc = load_docx("./data/BarackHusseinObamaWiki.docx")

doc_text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])

txt = load_text_file("./data/ObamaDanskeLex.txt")

st.write('We loaded the data from the two files.')

st.write('Data loaded successfully.')

# Input text from the user
user_input = st.text_area("Enter your text here:", "")

# --------------splitting them in to words------------

text1 = doc_text.split(" ")
text2 = txt.split(" ")

st.write('We split the data sets by all the spaces in the text.')

# ---------------Join the texts and and remove dublicates.----------------

corpus = set(text1).union(set(text2))

# Calculate the length of the corpus
corpus_length = len(corpus)

# Display the length of the corpus along with a message
st.write(f"The corpus contains {corpus_length} words/documents.")

# ---------------The document is now of type set----------------

dict1 = vect(text1, corpus)

dict2 = vect(text2, corpus)

df = pd.DataFrame([dict1, dict2])

st.write('We created a binary vector of word appearance in a sentence.')

st.write(df)

# --------------- convert the dataframe to a numpy array---------------

ar = df.to_numpy()

# --------------- calculate the cosine similarity---------------


cosim_simularity = cosim(ar[0], ar[1])

st.write(f'We calculated the cosine similarity between the two vectors.')
st.write(f'Cosine similarity: {cosim_simularity}')


st.write("Hello, world!")

