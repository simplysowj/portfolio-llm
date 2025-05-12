__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import streamlit as st
import os
from langchain.chains import RetrievalQA

from langchain_community.llms import OpenAI

from langchain.text_splitter import CharacterTextSplitter


from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import os
import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader, CSVLoader
from langchain_community.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import Chroma
# from langchain.prompts import PromptTemplate
from langchain.prompts import load_prompt
from streamlit import session_state as ss
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import uuid
import json
import time
from langchain.embeddings.openai import OpenAIEmbeddings

import datetime


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
    {"label": "Sample Project","url":"https://financeagenticai-qpny4rrjsvpjubga748d4a.streamlit.app/"},
    
    {"label": "GitHub", "url": "https://github.com/simplysowj"},
   
]

# Render the horizontal navbar
st.markdown(horizontal_navbar(navbar_links), unsafe_allow_html=True)
st.title("Resume Q&A Chatbot")
def is_valid_json(data):
    try:
        json.loads(data)
        return True
    except json.JSONDecodeError:
        return False


#if "mongodB_pass" in os.environ:
   # mongodB_pass = os.getenv("mongodB_pass")
#else: mongodB_pass = st.secrets["mongodb"]["mongodB_pass"]
# Setting up a mongo_db connection to store conversations for deeper analysis
#uri = f"mongodb+srv://simplysowj:{mongodB_pass}@cluster0.96b5s.mongodb.net/"
#uri = "mongodb+srv://simplysowj:"+mongodB_pass+"@cluster0.96b5s.mongodb.net/?retryWrites=true&w=majority"

#@st.cache_resource
#def init_connection():
 #   return MongoClient(uri, server_api=ServerApi('1'))
#client = init_connection()


#db = client['conversations_db']
#conversations_collection = db['conversations']

st.markdown("""
### How to get an OpenAI API Key

To use this chatbot, you'll need an OpenAI API key. Here's how to get one:

1. **Go to [OpenAI Platform](https://platform.openai.com/)**
   - Sign up or log in to your account

2. **Access API Keys**
   - Click your profile icon (top-right)
   - Select "View API keys"

3. **Create New Key**
   - Click "Create new secret key"
   - Name it (e.g., "ResumeGPT")
   - Copy the key (it starts with `sk-` and won't be shown again!)

4. **Enter it below** ⬇️
   - Paste in the sidebar input box
   - The app will verify it automatically

⚠️ **Important Notes:**
- Keys are sensitive - don't share them!
- Free tier has usage limits
- You may need to add payment method for continued use
""")
# Get OpenAI API key from user
openai_api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")

if not openai_api_key:
    st.warning("Please enter your OpenAI API key in the sidebar to continue.")
    st.stop()

# Check if the API key is valid by trying to create embeddings
try:
    test_embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    test_embeddings.embed_query("test")
    st.sidebar.success("API key is valid!")
except Exception as e:
    st.sidebar.error(f"Invalid API key. Error: {str(e)}")
    st.stop()
    



#Creating Streamlit title and adding additional information about the bot
st.title("Sowjanya's resumeGPT")
with st.expander("⚠️Disclaimer"):
    st.write("""This is a work in progress chatbot based on a large language model. It can answer questions about Sowjanya""")

path = os.path.dirname(__file__)


# Loading prompt to query openai
prompt_template = os.path.join(path, "templates", "template.json")  # More robust path handling
prompt = load_prompt(prompt_template)
#prompt = template.format(input_parameter=user_input)

# loading embedings
faiss_index = path+"/faiss_index"

# Loading CSV file
data_source = os.path.join(path, "data", "about_me.csv")


pdf_source = os.path.join(path, "data", "AI Ml Sowjanya.pdf")

# Function to store conversation
def store_conversation(conversation_id, user_message, bot_message, answered):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "conversation_id": conversation_id,
        "timestamp": timestamp,
        "user_message": user_message,
        "bot_message": bot_message,
        "answered": answered
    }
   # conversations_collection.insert_one(data)

embeddings=OpenAIEmbeddings(openai_api_key=openai_api_key)

#using FAISS as a vector DB
if os.path.exists(faiss_index):
        vectors = FAISS.load_local(faiss_index, embeddings,allow_dangerous_deserialization=True)
else:
    # Creating embeddings for the docs
    if data_source:
        # Load data from PDF and CSV sources
        pdf_loader = PyPDFLoader(pdf_source)
        pdf_data = pdf_loader.load_and_split()
        print(pdf_data)
        csv_loader = CSVLoader(file_path=data_source, encoding="utf-8")
        #loader.
        csv_data = csv_loader.load()
        data = pdf_data + csv_data
        vectors = FAISS.from_documents(data, embeddings)
        vectors.save_local("faiss_index")

retriever=vectors.as_retriever(search_type="similarity", search_kwargs={"k":6, "include_metadata":True, "score_threshold":0.6})
#Creating langchain retreval chain 
chain = ConversationalRetrievalChain.from_llm(llm = ChatOpenAI(temperature=0.0,model_name='gpt-3.5-turbo', openai_api_key=openai_api_key), 
                                                retriever=retriever,return_source_documents=True,verbose=True,chain_type="stuff",
                                                max_tokens_limit=4097, combine_docs_chain_kwargs={"prompt": prompt})


def conversational_chat(query):
    with st.spinner("Thinking..."):
        # time.sleep(1)
        # Be conversational and ask a follow up questions to keep the conversation going"
        result = chain({"system": 
        "You are a Art's ResumeGPT chatbot, a comprehensive, interactive resource for exploring Sowjanya  (Sowjanya) Bojja 's background, skills, and expertise. Be polite and provide answers based on the provided context only. Use only the provided data and not prior knowledge.", 
                        "question": query, 
                        "chat_history": st.session_state['history']})
    
    if (is_valid_json(result["answer"])):              
        data = json.loads(result["answer"])
    else:
        data = json.loads('{"answered":"false", "response":"Hmm... Something is not right. I\'m experiencing technical difficulties. Try asking your question again or ask another question about Sowjanya\'s professional background and qualifications. Thank you for your understanding.", "questions":["What is Sowjanya\'s professional experience?","What projects has Sowjanya worked on?","What are Sowjanya\'s career goals?"]}')
    # Access data fields
    answered = data.get("answered")
    response = data.get("response")
    questions = data.get("questions")

    full_response="--"

    st.session_state['history'].append((query, response))
    
    if ('I am tuned to only answer questions' in response) or (response == ""):
        full_response = """Unfortunately, I can't answer this question. My capabilities are limited to providing information about Sowjanya Bojja's professional background and qualifications. If you have other inquiries, I recommend reaching out to Sowjanya on [LinkedIn](https://www.linkedin.com/in/sowjanya-bojja/). I can answer questions like: \n - What is Sowjanya's educational background? \n - Can you list Sowjanya's professional experience? \n - What skills does Sowjanya possess? \n"""
        store_conversation(st.session_state["uuid"], query, full_response, answered)
        
    else: 
        markdown_list = ""
        for item in questions:
            markdown_list += f"- {item}\n"
        full_response = response + "\n\n What else would you like to know about Sowjanya? You can ask me: \n" + markdown_list
        store_conversation(st.session_state["uuid"], query, full_response, answered)
    return(full_response)

if "uuid" not in st.session_state:
    st.session_state["uuid"] = str(uuid.uuid4())

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []
    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        welcome_message = """
            Welcome! I'm **Sowjanya's ResumeGPT**, specialized in providing information about Sowjanya's professional background and qualifications. Feel free to ask me questions such as:

            - What is Sowjanya's educational background?
            - Can you outline Sowjanya's professional experience?
            - What skills and expertise does Sowjanya bring to the table?

            I'm here to assist you. What would you like to know?
            """
        message_placeholder.markdown(welcome_message)
        

if 'history' not in st.session_state:
    st.session_state['history'] = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me about Sowjanya"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        
        user_input=prompt
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        full_response = conversational_chat(user_input)
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
# Define the path to your local PDF file
pdf_file_path = "images/Sowjanya_AI.pdf"  

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
