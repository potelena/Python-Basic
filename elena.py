# To run, copy and paste the code below
# streamlit run elena.py --server.port 8080 --server.address 0.0.0.0

# streamlit official doc link:
# https://docs.streamlit.io/


import streamlit as st

title = "Clean Water"
st.title(title)

text = """
This is a game where you need to clean the water by pulling out dirty things and making sure its clean. 
After you make it clean, you need to give it to the other people or animals.
"""
st.write(text)

# name = st.text_input("Enter your name")
# st.write("Hello," ,name, ",lets talk to THE POTATO")

st.image("1.png")