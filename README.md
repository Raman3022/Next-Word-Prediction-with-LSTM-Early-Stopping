# Next-Word-Prediction-with-LSTM-Early-Stopping

Overview : 

This project implements a Next Word Prediction model using an LSTM (Long Short-Term Memory) neural network used for text generation, trained on William Shakespeare's Hamlet. The model uses deep learning techniques to generate text in the style of Shakespeare. It utilizes a tokenizer for text preprocessing and sequence padding to ensure consistent input length. The model is deployed as a web application using Streamlit.


# Features

1.Loads a pre-trained LSTM model (next_word_lstm.h5)

2.Utilizes a trained tokenizer (tokenizer.pickle) for text processing

3.Implements sequence padding to handle variable input lengths

4.Predicts the most likely next word based on the given input

5.Simple and interactive Streamlit UI for easy testing

# Requirements

To run this project, ensure you have the following dependencies installed:

tensorflow
pandas
scikit-learn
tensorboard
matplotlib
streamlit
scikeras
nltk 

# Usage

1. Run the Streamlit App

After installing the dependencies, navigate to the project directory and run:

streamlit run app.py

2. Enter Text & Predict

Type a sequence of words into the text input field.

Click the Predict Next Word button.

The model will generate and display the most likely next word.


# Model Architecture

The model is based on an LSTM neural network, commonly used for sequence modeling and text generation.



# Code Structure

app.py: The main application script using Streamlit.

next_word_lstm.h5: Trained LSTM model.

tokenizer.pickle: Tokenizer used for text processing.

# Configuration

System Information on which system is trained on - 

Processor: 13th Gen Intel(R) Core(TM) i7-13620H (16 CPUs) @ 2.4GHz

Memory: 16GB RAM 

Graphics: Nvedia Geforce RTX 4050 (Memory - 13964)

Total epoch trained on 100 with improved accuracy and degrading loss


# Future Improvements

Extend training dataset for better predictions.

Implement multi-word predictions.

Add GPU acceleration for faster inference.

Add more training time and increase number of epochs 

# Author

Raman Srivastava

License

This project is open-source and available under the MIT License.

