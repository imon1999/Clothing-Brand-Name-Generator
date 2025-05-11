import streamlit as st
import langchain_helper

st.title("Clothing Brand Name Generator")

clothing_style = st.sidebar.selectbox(
    "Enter Clothing Style",
    ("Streetwear", "Minimalist", "Vintage", "Luxury", "Sustainable", "Kids", "Sportswear", "Undergarments")
)

if clothing_style:
    response = langchain_helper.generate_clothing_brand_name_and_items(clothing_style)
    st.header(response['brand_name'].strip())
    keywords = response['keywords'].strip().split(",")
    st.write("**Categories**")
    for item in keywords:
        st.write("-", item.strip())
