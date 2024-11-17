import streamlit as st
import base64


def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
#local_css("style/style.css/")



st.title("📝 Resume")

pdf_path = "images/sowjanya_genai resume (1).pdf"

# Provide a download button for the PDF
with open(pdf_path, "rb") as pdf_file:
    pdf_bytes = pdf_file.read()
    st.download_button(
        label="Download Resume as PDF",
        data=pdf_bytes,
        file_name="Sowjanya_Data_science_latest_resume.pdf",
        mime="application/pdf"
    )

# Inform users about the download button
st.markdown(
    """
    Click the button above to download the resume as a PDF file.
    """,
    unsafe_allow_html=True
)


