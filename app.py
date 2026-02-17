import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello, Streamlit! It's my First Streamlit App")
st.write("Hello Ayush")
st.text("Lets start")

name=st.text_input("Enter your name")
if st.button("Greet"):
    st.write(f"Hello, {name}! Welcome to Streamlit.")

df=pd.DataFrame(np.random.randn(10,2),columns=['A','B'])
st.line_chart(df)
st.bar_chart(df)

st.sidebar.title("Navigation")
st.image("https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png", width=200, caption="Google Logo")
st.video("https://www.youtube.com/shorts/hHzfUVvd6kU?feature=share")

uploaded_file=st.file_uploader("upload a file")
if uploaded_file is not None:
    st.write(
        {
            "name": uploaded_file.name,
            "type": uploaded_file.type,
            "size_bytes": uploaded_file.size,
        }
    )
    st.download_button(
        "Download uploaded file",
        data=uploaded_file.getvalue(),
        file_name=uploaded_file.name,
        mime=uploaded_file.type,
    )

st.header("This is a header")
st.subheader("This is a subheader")

st.markdown("**Bold**, *Italic*, `Code`, [Link](https://streamlit.io)")
st.code("for i in range(5): print(i)", language="python")

st.text_input("What's your name?")
st.text_area("Write something...")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100)
st.selectbox("Select a fruit", ["Apple", "Banana", "Mango"])
st.multiselect("Choose toppings", ["Cheese", "Tomato", "Olives"])
st.radio("Pick one", ["Option A", "Option B"])
st.checkbox("I agree to the terms")

if st.checkbox("Show Details"):
    st.info("Here are more details...")

option = st.radio("Choose view", ["Show Chart", "Show Table"])

if option == "Show Chart":
    st.write("Chart would appear here")
else:
    st.write("Table would appear here")

with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

if submitted:
    st.success(f"Welcome, {username}!")

col1, col2 = st.columns(2)

with col1:
    st.button("Press me in Column 1")

with col2:
    st.button("Press me in Column 2")

with st.expander("See Explanation"):
    st.write("Here is a hidden message inside the expander.")



