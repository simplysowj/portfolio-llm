import streamlit as st
# Sidebar
st.sidebar.markdown("Developed by Sowjanya")
st.sidebar.markdown("Contact: [simplysowj@gmai.com](mailto:simplysowj@gmai.com)")
st.sidebar.markdown("GitHub: [Repo](https://github.com/simplysowj)")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    
local_css("style/style.css")
def display_projects():
    st.title("Some of my Projects")

    projects = [
        {
            "title": "AI Intern, Mentorness --Generative AI",
            "duration": "Feb 2024 - Mar 2024",
            "description": """
            Developed a dynamic ATS Resume Expert application using Gemini-pro-vision during my internship with Mentorness. 
            Utilizing OpenAI's Generative AI capabilities, it analyzes PDF resumes against job descriptions, offering evaluations on alignment, 
            missing keywords, and candidate suitability. This Streamlit app showcases a versatile portfolio template integrating features like 
            resume parsing, an AI chatbot powered by OpenAI, and interactive elements for comprehensive personal branding, demonstrating 
            proficiency in leveraging diverse technologies for impactful web experiences.
            """,
            "github_link": "https://github.com/simplysowj/Mentorness",
            "video_link": "https://www.linkedin.com/posts/sowjanya-bojja_atsresume-streamlit-resumeparser-activity-7173455333477064704-WaeO?utm_source=share&utm_medium=member_desktop"  
        },
         {
            "title": "Big Data Engineering Project(Kafka,Pyspark via Zepplin using Docker)",
            "duration": "Feb 2024 - Mar 2024 as part of academics",
            "description": """Developed an end-to-end sentiment analysis workflow using Apache Spark, Kafka, and PySpark, with Docker for container management and Streamlit for visualization.
            Trained sentiment analysis models in Spark via Zeppelin and integrated results with MySQL for scalable and robust data storage and analysis.
            Created a user-friendly web app with Streamlit to visualize sentiment trends, enhancing accessibility and actionable insights from large-scale datasets.""",
            "github_link": "https://github.com/simplysowj/bigdataenggproject",
            "video_link": "https://www.linkedin.com/posts/sowjanya-bojja_sentimentanalysis-apachespark-kafka-activity-7186393653991415808-2qUG?utm_source=share&utm_medium=member_desktop"
        },
        {   
            "title":"Analyzed sales data using Databricks, PySpark, and Matplotlib. ",
            "duration": "Feb 2024 - Mar 2024 as part of academics",
            "description": """
            Analyzed sales data using Databricks, PySpark, and Matplotlib. Conducted Exploratory Data Analysis (EDA) to uncover insights and trends, processed large datasets efficiently, and created interactive visualizations showcasing sales trends and key metrics.
            """,
            "github_link": "https://lnkd.in/eFYi_DQv",
            "video_link": "https://www.linkedin.com/posts/sowjanya-bojja_databricks-pyspark-pyspark-activity-7177390039205597185-lXg6?utm_source=share&utm_medium=member_desktop"
        },
        {
            "title": "Bharat Intern - Data Science Intern",
            "duration": "Jan 2024 - Feb 2024",
            "description": """
            Implemented an SMS spam/ham classifier leveraging machine learning techniques to accurately classify text messages. 
            Additionally, developed a Titanic data classification model to predict survival outcomes using passenger data.
            """,
            "github_link": "https://github.com/simplysowj/CatVsDog_Classifier-SpamDetector",
             "video_link":"https://www.linkedin.com/posts/sowjanya-bojja_tensorflow-flask-deeplearning-activity-7163954448375996417-BExp?utm_source=share&utm_medium=member_desktop"
        },
        {
            "title": "Cognifyz Technologies ---ML Intern",
            "duration": "Jan 2024 - Feb 2024",
            "description": """
            Implemented ML algorithm for Income prediction and Gold price Prediction.
            """,
            "github_link": "https://github.com/simplysowj/Gold-Price-Prediction-including-Flask-app",
            "video_link": "https://www.linkedin.com/posts/sowjanya-bojja_internshipjourney-goldpriceprediction-activity-7164817502026321920-712k?utm_source=share&utm_medium=member_desktop"
        },
        {
            "title": "Innomatics Research LABS (3 Months)",
            "duration": "Internship",
            "description": """
            Demonstrated proficiency in Python problem-solving on HackerRank, application development using FLASK and Streamlit, along with expertise in statistics, ML algorithms with hyperparameter tuning, and advanced techniques such as BERT vectorization. Additionally, showcased competence in experiment tracking, model management with MLflow, workflow orchestration with Prefect, NLP, and cloud deployment on platforms like Heroku and GitHub. Received a Letter of Recommendation for my performance.
            """,
            "github_link": [
                "https://github.com/simplysowj/Quora_duplicate_question_detector",
                "https://github.com/simplysowj/Internship_july_2022"
            ],
            "video_link": "https://www.linkedin.com/posts/sowjanya-bojja_mlflow-mlops-ml-activity-6989568784457973760-RggX?utm_source=share&utm_medium=member_desktop"
        },
        {
            "title": "Internshala Trainings - NLP Projects",
            "duration": "",
            "description": """
            Auto correct project (Spelling corrector)
            """,
            "github_link": [
                
                "https://github.com/simplysowj/NLP_projects"
            ],
            "video_link": ""
        },
        {
            "title": "Tableau Project - Bikehaven project",
            "duration": "",
            "description": "",
            "github_link": "https://github.com/simplysowj/tableau",
            "video_link": "https://www.linkedin.com/posts/sowjanya-bojja_activity-7146645292652625921-uvu9?utm_source=share&utm_medium=member_desktop"
        },
        {
            "title": "SQL Project - IPL Data Analysis using SQL and Data visualization using Excel",
            "duration": "",
            "description": """
            Analysis of IPL data using SQL (PostgreSQL) and Data visualization using Excel.
            """,
            "github_link": "https://github.com/simplysowj",
            "video_link": "https://www.linkedin.com/posts/sowjanya-bojja_successfully-finished-ipl-data-analysis-usingactivity-7130554150039257088-LGf1?utm_source=share&utm_medium=member_desktop"
        },
        {
            "title": "Advanced Excel Project - Fitbit",
            "duration": "",
            "description": """
            Analysis of Fitbit fitness tracker data to deliver marketing and business solutions to WeFit and its subsidiaries.
            """,
            "github_link": "https://github.com/simplysowj/fitbit",
            "video_link": "https://www.linkedin.com/posts/sowjanya-bojja_analysis-of-fitbit-fitness-tracker-data-to-activity-7116596211960221696-KafI?utm_source=share&utm_medium=member_desktop"
        },
        {
            "title": "CU major project--(NLP,DL,Generative AI)",
            "duration": "MSC in Data Science",
            "description": """
            Developed an interactive chatbot capable of generating captions for images and audio. Utilized advanced AI techniques, including image captioning (using Deep learning and NLP) and audio generation with Gen AI, to enhance user experience.
            """,
            "github_link": "",
            "video_link": "https://www.linkedin.com/posts/sowjanya-bojja_innovation-accessibility-ai-ugcPost-7197697478962335744-awtm?utm_source=share&utm_medium=member_desktop"
        },
        {
            "title": "CU Project -- Springboot,MongoDB and React(Microservices) ",
            "duration": "MSC in Data Science",
            "description": """
            Developed a movie review application using MongoDB, Java, Spring Boot, and React, featuring a loosely coupled architecture for independent evolution of client and server code, leveraging microservices for efficient business function handling. Spring Boot was chosen for its rapid development capabilities in the microservices landscape.
            """,
            "github_link": "",
            "video_link": "https://www.linkedin.com/posts/sowjanya-bojja_i-am-happy-to-share-a-movie-review-application-activity-7160443895137419264-SGYf?utm_source=share&utm_medium=member_desktop"
        },
        {
            "title": " CU Minor Project---Big Data Engineering (Kafka,pyspark,Mysql with DL using Docker and Zepplin)",
            "duration": "MSC in Data Science",
            "description": """
            Implemented a fraud detection system using big data concepts such as Kafka, PySpark, and MySQL with Machine learning algorithms. Developed a user-friendly interface using Streamlit and incorporated Gen AI for front-end enhancement.
            """,
            "github_link": "",
            "video_link": "https://www.linkedin.com/posts/sowjanya-bojja_financialanalysis-frauddetection-datavisualization-activity-7197954843980783616-G48c?utm_source=share&utm_medium=member_desktop"
        }
       ]

    for project in projects:
        st.subheader(project["title"])
        st.write(f"**Duration:** {project['duration']}")
        st.write(project["description"])
        if project["github_link"]:
            if isinstance(project["github_link"], list):
                for link in project["github_link"]:
                    st.write(f"[GitHub Repository]({link})")
            else:
                st.write(f"[GitHub Repository]({project['github_link']})")
        if project["video_link"]:
            st.write(project["video_link"])



display_projects()
