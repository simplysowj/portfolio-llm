import streamlit as st
from PIL import Image

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    
local_css("style/style.css")
        



img_4 = Image.open("images/4.png")
img_5 = Image.open("images/5.png")
img_6 = Image.open("images/6.png")
img_7 = Image.open("images/7.png")
img_8 = Image.open("images/8.png")
img_9 = Image.open("images/9.png")
img_10 = Image.open("images/nlp.png")
img_11=Image.open("images/marks.png")

st.title("🫶 Certifications")

col1, col2, col3,col4,col5,col6 = st.columns(6)

st.image(img_4)
   
st.image(img_5)

st.image(img_6)
st.image(img_7)
   
st.image(img_8)
st.image(img_9)
st.image(img_10)
st.image(img_11)

