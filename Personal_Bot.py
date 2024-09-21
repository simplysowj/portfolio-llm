__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import streamlit as st
import os
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# Streamlit app configuration
st.set_page_config(page_title='Resume Q&A Chatbot', layout='wide')

# Sidebar
st.sidebar.markdown("Developed by Sowjanya")
st.sidebar.markdown("Contact: [simplysowj@gmai.com](mailto:simplysowj@gmai.com)")
st.sidebar.markdown("GitHub: [Repo](https://github.com/simplysowj)")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    
local_css("style/style.css")
# Main Title

# Function to create a horizontal navbar
def horizontal_navbar(links):
    nav_html = """
    <style>
    .navbar {
        overflow: hidden;
        
        display: flex;
        justify-content: center;
    }

    .navbar a {
        float: left;
        display: block;
        color: white;
        text-align: center;
        padding: 14px 20px;
        text-decoration: none;
        font-size: 17px;
    }

    .navbar a:hover {
        background-color: #ddd;
        color: black;
    }
    </style>
    <div class="navbar">
    """
    for link in links:
        nav_html += f'<a href="{link["url"]}" {"download" if link["label"] == "Resume" else ""}>{link["label"]}</a>'
    nav_html += "</div>"
    return nav_html

# Define links for the navbar
navbar_links = [
    {"label": "Medium Article", "url": "https://medium.com/@simplysowj"},
    {"label": "Sample Project","url":"https://blippy-souji.streamlit.app/"},
    {"label": "LinkedIn", "url": "https://www.linkedin.com/in/sowjanya-bojja/"},
    {"label": "GitHub", "url": "https://github.com/simplysowj"},
   
]

# Render the horizontal navbar
st.markdown(horizontal_navbar(navbar_links), unsafe_allow_html=True)
st.title("Resume Q&A Chatbot")
st.markdown("## How to use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) in the sidebar and hit enter🔑\n"  # noqa: E501
            "2.If you dont have api key please click this link https://www.guvi.in/rag/d0dfa9d5-3d3f-4e7d-a5e9-dbf8e3c5f4bd "
           )

api_key = st.sidebar.text_input('Enter your OpenAI API Key and hit Enter', type="password")
# Input fields for the OpenAI API key
#api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Define the path to your local PDF file
pdf_file_path = "images/Sowjanya_AI.pdf"  

# Text input for the question
question = st.text_input("Enter your question about the resume:")

# Define the fixed chain type and other configurations
chain_type = 'stuff'
chunk_size = 1000  # Fixed chunk size

def load_and_process_pdf(file_path):
    """Load and process the PDF to create a vector store."""
    # Load document from PDF
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # Split the documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    # Create embeddings and vectorstore
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(texts, embeddings)
    
    return db

def get_qa_answer(query):
    """Generate the answer to the query using the QA chain."""
    # Ensure the API key is set
    os.environ["OPENAI_API_KEY"] = api_key

    # Process the PDF
    db = load_and_process_pdf(pdf_file_path)

    # Create retriever and QA chain
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 2})  # Using k=2 as an example
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(), chain_type=chain_type, retriever=retriever, return_source_documents=True
    )

    # Define the custom prompt
    name = "Sowjanya"
    pronoun = "her"
    prompt = f"""
    You are Buddy, an AI assistant dedicated to assisting {name} in her job search by providing recruiters with relevant and concise information. 
    If you do not know the answer, politely admit it and let recruiters know how to contact {name} to get more information directly from {pronoun}. 
    Don't put "Buddy" or a breakline in the front of your answer.
    """

    # Get the answer
    try:
        result = qa_chain({"query": query, "prompt": prompt})
        
        if "I don't know" in result.get("result", ""):

            result["result"] = f"Unfortunately, I couldn't find specific information on that topic. For more details or further assistance, please feel free to contact {name} directly at [simplysowj@gmai.com](mailto:simplysowj@gmai.com)."
        
    except Exception as e:
        result = {"result": f"An error occurred: {str(e)}"}

    return result

if st.button("Run"):
    if api_key and question:
        with st.spinner("Processing..."):
            result = get_qa_answer(question)

        # Display the results
        st.write("**Answer:**")
        st.write(result["result"])

        
    else:
        st.error("Please provide all required inputs.")
with st.container():
    col1,col2 = st.columns([8,3])
   
with col2:
    st.subheader("📨 Contact Me")
    contact_form = f"""
    <form action="https://formsubmit.co/simplysowj@gmail.com" method="POST">
        <input type="hidden" name="_captcha value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
