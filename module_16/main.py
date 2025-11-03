import streamlit as st

if st.button("Press me"):
    st.write("Why did you press me?")

if st.checkbox("Check me bro"):
    st.write("Why did you check me?")

user_input = st.text_input("Enter Text", "Sample Text")
st.write("You wrote: ", user_input)

age = st.number_input("Enter your age", min_value=0, max_value=100)
st.write(f"Your age is {age} ")

message = st.text_area("Write a text")
st.write(f"You wrote {message}")