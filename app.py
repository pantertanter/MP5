import streamlit as st
from data_loader import (load_docx, load_text_file,
                         vect)
import pandas as pd
from cosimfunc import cosim
from sentence_transformers import SentenceTransformer, util
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



# Load the data---------------------------------------

doc = load_docx("./data/BarackHusseinObamaWiki.docx")

doc_text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])

# Pass the content to load_text_file
txt = load_text_file("./data/ObamaDanskeLex.txt")

st.write('We loaded the data from the two files.')

st.write('Data loaded successfully.')



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


# ------------------function to ask a question and get an answer----------------

st.write("Hello, world!")

# Load pre-stored text data


# Create an empty DataFrame to store text data
pre_stored_data = pd.DataFrame(columns=["text"])
#st.write(pre_stored_data) - needed to check dataframe

# Append the text from the variable txt to the DataFrame
pre_stored_data = pre_stored_data._append({"text": txt}, ignore_index=True)


# Append text from .doc document
pre_stored_data = pre_stored_data._append({"text": doc_text}, ignore_index=True)

# Vectorize the pre-stored text data using TF-IDF
vectorizer = TfidfVectorizer()
vectorized_pre_stored_data = vectorizer.fit_transform(pre_stored_data['text'])


# Text input field for user to enter text
user_input = st.text_area("Enter your text:", "")
if st.button("Find Similar Texts"):
    # Vectorize user input
    vectorized_user_input = vectorizer.transform([user_input])

    # Calculate cosine similarity between user input and pre-stored text data
    similarities = cosine_similarity(vectorized_user_input, vectorized_pre_stored_data)

    # Sort similarities and get indices of top three related pieces of text
    top_three_indices = similarities.argsort(axis=1)[0][-3:][::-1]

    # Output top three related pieces of text
    st.subheader("Top 3 Related Texts:")
    for index in top_three_indices:
        similarity_score = similarities[0][index]
        related_text = pre_stored_data.iloc[index]['text']
        st.write(f"Similarity Score: {similarity_score:.2f}")
        st.write(related_text)



st.write("What could be the real world application of this app?")
st.write("Plagiarism detection, Content recommendation (books etc.) Customer Support (help articles)")
