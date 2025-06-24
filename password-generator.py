import streamlit as st
import random
import string

def password_generator(length,use_digits,use_special_char):
    characters = string.ascii_letters

    if use_digits: 
        characters += string.digits # add digits(0-9)

    if use_special_char:
        characters += string.punctuation # add special characters (! @ # $ % ^ & *)
    
    if not characters:
        characters = string.ascii_letters # making error free

    return ''.join(random.choice(characters) for _ in range(length)) # return a random string of given length       


st.title("Password generator")

length = st.slider("select Password Length",min_value = 4, max_value = 30, value = 12) # last one (value) tells that by default how much length we want.

use_digits = st.checkbox("Include digits")

use_special_char = st.checkbox("Include special characters")

if st.button("Generate Password"): # if button(Generate Password) is clicked
    password = password_generator(length,use_digits,use_special_char) # streamlit UI is understanding these parameters as we have list them above using st. module
    st.success(f"Generated password: {password}")
else:
    st.write("Click the button to generate password") # if button is not clicked, it will


st.write("----------------")

st.write("Build with 💗| by [Hamza Atif](https://github.com/HamzaAtif)")