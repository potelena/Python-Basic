# To run, copy and paste the code below
# streamlit run elena.py --server.port 8080 --server.address 0.0.0.0

# streamlit official doc link:
# https://docs.streamlit.io/


import streamlit as st

st.title("Talk with THE POTATO")
st.write("This is sample text")

name = st.text_input("Enter your name")
st.write(name)

st.write('Hello,' ,name, "Welcome")
