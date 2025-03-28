import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


# load the LSTM model
model = load_model("next_word_lstm.h5")

# load the tokenizer
with open("tokenizer.pickle", "rb") as f:
    tokenizer = pickle.load(f)

# function to predict the next word


def predict_next_word(model, tokenizer, text, max_sequence_len):
    token_list = tokenizer.texts_to_sequences([text])[0]
    if len(token_list) >= max_sequence_len:
        token_list = token_list[-(max_sequence_len - 1) :]
    token_list = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding="pre")
    predicted = model.predict(token_list, verbose=0)
    predicted_word_index = np.argmax(predicted, axis=1)
    for word, index in tokenizer.word_index.items():
        if index == predicted_word_index:
            return word
    return None


# streamlit app

st.title("Next Word Prediction with LSTM & Early Stopping")
input_text = st.text_input("Enter a sequence of words:", "To be or not to be")
if st.button("Predict Next Word"):
    next_word = predict_next_word(model, tokenizer, input_text, 5)
    st.write(f"The next word is: {next_word}")
