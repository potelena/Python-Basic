# To run, copy and paste the code below
# streamlit run elena.py --server.port 8080 --server.address 0.0.0.0

# streamlit official doc link:
# https://docs.streamlit.io/


import streamlit as st

title = "Talk with THE POTATO"
st.title(title)

text = "This is the chatting place to have a nice chat with THE POTATO"
st.write(text)

name = st.text_input("Enter your name")
st.write("Hello," ,name, ",lets talk to THE POTATO")

