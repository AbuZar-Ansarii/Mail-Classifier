import streamlit as st
import pickle

model = pickle.load(open('Filter Spam.pkl','rb'))

def clean_text(text):
    text = text.lower() # change text to lowercase
    text = text.split() # convert word to token

    # y = []
    # for i in text:
    #     if i.isalnum():
    #         y.append(i)
    return text


# start making webApp
st.title("Spam Mail/Sms Filter")
user_input = st.text_area("Enter Text")
cleaned_text = clean_text(user_input)

if st.button("click"):
    result = model.predict(cleaned_text)[0]
    if result == 1:
        st.header("Spam Message")
    else:
        st.header("Not Spam")

