import streamlit as st


def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    
local_css("style/style.css")

# Technical Skills Section
st.subheader("🛠 Technical Skills")

st.markdown("""
            <div style=" padding: 10px; border-radius: 5px;">
                <ul style="list-style-type: none; padding: 0;">
                    <li><b>Programming Languages:</b> Python, Java, C</li>
                    <li><b>Web Development:</b> HTML, CSS, JavaScript, Bootstrap</li>
                    <li><b>JavaScript Libraries & Frameworks:</b> Node.js, React.js</li>
                    <li><b>Java Framework:</b> SpringBoot</li>
                    <li><b>Microservices & Containers:</b> Docker</li>
                    <li><b>Big Data Engineering:</b> Kafka, PySpark</li>
                    <li><b>Gen AI Skills:</b> LLM (Large Language Model)</li>
                    <li><b>Data Visualization:</b> Tableau, Excel, Matplotlib, Seaborn</li>
                    <li><b>Web Frameworks:</b> Flask, Streamlit</li>
                    <li><b>GUI Development:</b> Swing</li>
                    <li><b>Other Technologies:</b> Microservices Architecture</li>
                    <li><b>Tools:</b> Git, Anaconda, Jupyter notebook/Colab, VS Code, IntelliJ IDEA</li>
                    <li><b>Databases:</b> MySQL, PostgreSQL, Toad, MongoDB Atlas</li>
                    <li><b>Soft Skills:</b> Problem Solving, Team Collaboration, Communication, Time Management</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
# Education Section
st.subheader("🎓 Education")
st.write("""
            -**Master of Science (MSC) in Data Science Chandigarh University, India  July 2022 - August 2024**
            -**Relevant Coursework **: Python Programming, Calculus and Linear Algebra, Applied Probability and Statistics, 
                Data Analysis and Visualization, Communication and Soft Skills, Machine Learning, SQL Programming, 
                Advanced Machine Learning, Advanced Database Management, Deep Learning, Optimization, Natural Language Processing,
                Web Technologies,Cloud Native Development,Java Programming,Data Structures and algorithms,NLP,
                Applied Business Analytics,Data Mining and Data warehousing,data Engineering.
            - **Academic Projects & Papers **:
            Academic Papers
            https://medium.com/@simplysowj
            -**Projects **:
                Big Data Engineering and Gen AI Project(Kafka,Pyspark via Zeppelin using Docker) 
                Sentiment Analysis
                https://github.com/simplysowj/bigdataenggproject
                Implemented a fraud detection system using big data concepts such as Kafka, PySpark, and MySQL with Machine learning algorithms. 
                Developed a user-friendly interface using Streamlit and incorporated Gen AI for front-end enhancement.
                https://github.com/simplysowj/bigdata_fraud_detection
                Image Captioning with OCR and GenAI
                Developed an interactive chatbot capable of generating captions for images and audio with Text in the image.
                Utilized advanced AI techniques, 
                including image captioning (using Deep learning and NLP) and audio generation with Gen AI, to enhance user experience.
                https://github.com/simplysowj/OCR_Imagecaptioning_openai
                EDA with DataBricks
                worked on a project where I analyzed sales data using Databricks, hashtag#PySpark, and hashtag#Matplotlib.
                https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/1123303988966450/1736356871005362/5428641177518963/latest.html
                Movie Review App
                Developed a movie review application using MongoDB, 
                Java, Spring Boot, and React, featuring a loosely coupled architecture for independent evolution 
                of client and server code, leveraging microservices for efficient business function handling.
                Spring Boot was chosen for its rapid development capabilities in the microservices landscape.
                https://github.com/simplysowj/Microservices
             
        -**Bachelor of Technology (B. Tech) in Electronics and Communications –JNTU, India.    2002 - 2006**

        """)
        
# Advanced Skills Section
st.subheader("🔍 Advanced Skills")
st.write("""
        - **Machine Learning & Deep Learning**:
            - **Libraries**: NumPy, Pandas, Scikit-learn, NLTK, TensorFlow, PyTorch
            - **Techniques**: Data Exploration & Analysis, Data Modelling, Statistics and Probability, Linear Regression, Gradient Descent, Logistic Regression, Regularization, SVM, KNN, Decision Trees, Random Forest, Ensemble Techniques, Bagging & Boosting, Cross-Validation, Cluster Analysis, Hyperparameter Tuning, Experiment Tracking and Model Management using MLflow, MLOps
            - **NLP Techniques**: Tokenization, Bag of Words, Stemming, Lemmatization, POS Tagging, TF-IDF, BERT, Word2Vec, GloVe
            - **Deep Learning**: Neural Network Architectures (CNN, RNN, LSTM), Computer Vision (Image Classification, Object Detection, Image Segmentation), NLP Tasks (Sentiment Analysis, Text Classification, Language Modeling, Generative Adversarial Networks), Optimization Techniques (Gradient Descent)
        """)


#Industry Experience:
st.subheader("Previous Industry Experience in TCS , India")
st.write("""
        -**Plsql Developer Tools**:
                TOAD 7.6.0.11, PL/SQL Developer, Forms 61, Reports 6i
        -**Company TCS**:
            -**Client**: Electronic Arts-India Location Bangalore, India (2010 to 2014) (Nov 2010 May2014)
            -**Client**: Tata TeleServices Limited - India (2008 to 2010) Mar 2008-Oct 2010
            """)
    



st.markdown(
    """
    ### About Sowjanya:
    Sowjanya is a seasoned professional with expertise in AI, Data Science technologies. Holding a Post grad degree in data Science from the University of Chandigarh (2024), Sowjanya is committed to delivering innovative solutions.

    ### Work Experience:
    Data Science Intern and a Final year student

    ### Career Goal:
    Sowjanya's career goal is to leverage their expertise in AI and emerging technologies to drive meaningful innovation and create solutions that positively impact businesses and society.

    ### Skills: 
    AI, Data Science, Web technologies, Python, React JS, Spring Boot, and Big Data engineering

    ### Certification:
    - Certified Data Scientist

    ### Achievements:
    - LOR for the Internship

    ### Contact:
    - [LinkedIn](https://www.linkedin.com/in/sowjanya-bojja/)
    - Phone: 6692974674
    - Location: USA

    ### Strengths and Advantages:
    Sowjanya's strengths lie in a profound passion for technology, innovative problem-solving, and client-centric solutions.

    ### Weaknesses and Disadvantages:
    Sowjanya's unwavering pursuit of excellence may occasionally lead to in-depth analysis, but it ensures the delivery of high-quality services.

    ### Interests and Hobbies:
    Sowjanya's passion for technology extends into leisure hours, where they delve into the cutting-edge realm of GenAI, continuously pushing the boundaries of what can be achieved in various projects. In addition, she finds joy in the simple pleasures of life, solving puzzles, playing chess, and listening to music.

    ### Portfolio:
    Explore Sowjanya's portfolio, showcasing expertise and tailored solutions. This website also serves as a showcase for some of Sowjanya's remarkable projects. Constructed using generative AI and Python, the website aims to inspire visitors with innovative ideas on seamlessly integrating generative AI into their own portfolio websites. Feel free to explore and ignite your creativity!

    ### Availability:
    Sowjanya is actively seeking new opportunities and is ready to start immediately.

    ### References:
    References are available upon request.

    ### Certifications:
    - Certified Data Scientist
    - Certified Machine Learning Specialist

    ### Projects:
    - Fraud Detection System using LSTM Autoencoders and Spark-Kafka Integration.
    - Real-time Analytics Dashboard using Streamlit and Plotly.

    ### Publications:
    - Article on Machine Learning Best Practices, Medium.
    - Research Paper on Anomaly Detection, IEEE.

    ### Hobbies:
    - Blogging about data science and machine learning.
    - Participating in hackathons and coding competitions.

    ### Education:
    - M.S.C in Data Science
    """, unsafe_allow_html=True
)
