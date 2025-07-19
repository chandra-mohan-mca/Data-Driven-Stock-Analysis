import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Data-Driven Stock Analysis",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
    <h1 style='background-color: #4CAF50; text-align: center; box-shadow: 4px 4px 20px rgba(0,0,0,0.3); font-weight: bold; color: white; padding: 10px; border-radius: 10px;'>
        📊 Data-Driven Stock Analysis
    </h1>
""", unsafe_allow_html=True)
 

st.markdown(
    """<hr style="height:3px;border:none;color:#FF6347;background-color:#FF5733;" />""",
    unsafe_allow_html=True,
)

import base64

def get_base64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_path = r"c:\Users\vnave\Pictures\Data-Visualisation-Benefits-Techniques-and-Best-Courses-1.webp"  # ✅ Use raw string
img_base64 = get_base64_image(img_path)

st.markdown(
    f"""
    <img src="data:image/jpg;base64,{img_base64}" width="950" height="400" style='box-shadow: 4px 4px 25px rgba(0,0,0,0.3); border-radius: 10px;'>
    """, unsafe_allow_html=True  # ✅ comma is correct here
)