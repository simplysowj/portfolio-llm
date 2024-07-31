import streamlit as st
import base64


def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css/")



st.title("📝 Resume")

pdf_path = "images/Sowjanya_AI_resume.pdf"



# Inform users about the download button
st.markdown(
    """
    Click the button above to download the resume as a PDF file.
    """,
    unsafe_allow_html=True
)

with open("images/Sowjanya_AI_resume.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
      pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
      st.markdown(pdf_display, unsafe_allow_html=True)
  
