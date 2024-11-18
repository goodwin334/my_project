import streamlit as st

st.header('Tossing a Coin')

number_of_trials = st.slider('Number of trials?', 1, 1000, 10)
start_button = st.button('Run')

if start_button:
    st.write(f'Running the experiment of {number_of_trials} trials.')

<<<<<<< HEAD
st.write('It is not a functional application yet. Under construction.')
=======
st.write('It is not a functional application yet. Under construction.')
>>>>>>> e9ce7c1bbd5962f362d667e2608e0e6697b9579a
