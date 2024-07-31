import streamlit as st
from PIL import Image


def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        

local_css("style/style.css")



img_1 = Image.open("images/i1.png")
img_2 = Image.open("images/i2.png")
img_3 = Image.open("images/i3.png")
img_4 = Image.open("images/i4.png")
img_5 = Image.open("images/i5.png")

st.title("Internships")

col1, col2, col3 = st.columns(3)

with col1:
   st.image(img_1)
   
with col2:
   st.image(img_2)

with col3:
   st.image(img_3)
with col3:
   st.image(img_4)
with col3:
   st.image(img_5)
