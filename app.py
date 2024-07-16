import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
from st_on_hover_tabs import on_hover_tabs
#import requests
#from streamlit_lottie import st_lottie
from PIL import Image
#import streamlit_analytics
import base64
from streamlit_extras.mention import mention
from streamlit_extras.app_logo import add_logo
import sqlite3
#from bs4 import BeautifulSoup
from streamlit_extras.echo_expander import echo_expander

#test

# Set page title
st.set_page_config(page_title="Mustafa Mujahid", page_icon = "desktop_computer", layout = "wide", initial_sidebar_state = "auto")

# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

footer = """
footer{
    visibility:visible;
}
footer:after{
    content:'Copyright © 2024 Mustafa Mujahid';
    position:relative;
    color:black;
}
"""
# PDF functions
def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="400" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_link(pdf_url, link_text="Click here to view PDF"):
    href = f'<a href="{pdf_url}" target="_blank">{link_text}</a>'
    return href


# Add custom CSS for button styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #f5f5dc;  /* Primary color */
        color: darkorange;  /* Font color */
        border: none;
        border-radius: 5px;
        padding: 12px 20px;
        cursor: pointer;
    }
    }
    .stButton>button:hover {
        background-color: #e5e5d1;  /* Slightly darker shade for hover effect */
    }
    </style>
""", unsafe_allow_html=True)

def styled_download_button(label, file_path, color="#f5f5dc", hover_color="#e5e5d1", font_color="darkorange"):
    with open(file_path, "rb") as file:
        # Generate the download button
        button_html = f"""
        <a download="{file_path}" href="data:file/{file_path};base64,{file.read().encode('base64').decode()}">
            <button style="background-color: {color}; color: {font_color}; border: none; border-radius: 5px; padding: 12px 20px; cursor: pointer;">
                {label}
            </button>
        </a>
        """
    st.markdown(button_html, unsafe_allow_html=True)



# Load assets
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# Assets for about me
img_utown = Image.open("image_collection/about_me/utown.jpg")
img_lh = Image.open("image_collection/profile_photo/profile.jpg")
#Assets for competitions
logithon = Image.open("image_collection/competition/logithon_stage.jpg")
dmce_hackathon = Image.open("image_collection/competition/dmce_hackathon.jpg")
prakalp_2k23 = Image.open("image_collection/competition/prakalp.jpg")
alice = Image.open("image_collection/competition/alice.jpg")
rd_national = Image.open("image_collection/competition/rd_national.jpg")
# Assets for education
dmce = Image.open("image_collection/Education/DMCE.jpeg")
mumbai_uni = Image.open("image_collection/Education/mumbai_uni.png")
ssjp = Image.open("image_collection/Education/ssjp.jpg")
national = Image.open("image_collection/Education/national_copy.png")
# Assets for experiences
img_bitmetrix = Image.open("image_collection/Experience/pneucon_valves.jpg.png")
img_groundup = Image.open("image_collection/Experience/tiranga_textiles.jpg")
img_hedgedrip = Image.open("image_collection/Experience/hedgedrip.jpg")
# Assets for projects
image_names_projects = ["xparse", "urgpt", "fragabs", "datafabric", 
                         "carvana"]
images_projects = [Image.open(f"image_collection/projects/{name}.{'jpeg' if name not in ('map', 'gephi', 'health') else 'png'}") for name in image_names_projects]
# Assets for volunteering
image_names_vol = ["gdsclogo", "sih"]
images_vol = [Image.open(f"image_collection/volunteering/{name}.{'jpg' if name not in ('map', 'gephi', 'health') else 'png'}") for name in image_names_vol]

def social_icons(width=24, height=24, **kwargs):
    icon_template = '''
    <a href="{url}" target="_blank" style="margin-right: 20px; display: inline-block;">
        <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
    </a>
    '''

    icons_html = ""
    for name, url in kwargs.items():
        icon_src = {
            #"youtube": "https://img.icons8.com/ios-filled/100/ff8c00/youtube-play.png",
            "linkedin": "https://img.icons8.com/fluency/48/linkedin.png",
            #"github": "https://img.icons8.com/ios-filled/100/ff8c00/github--v2.png",
            "medium": "https://img.icons8.com/ios-filled/50/medium-logo.png",
            "email": "https://img.icons8.com/3d-fluency/94/mail.png"
        }.get(name.lower())

        if icon_src:
            icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

    # Remove the last margin-right for the last icon
    icons_html = icons_html.rstrip('</a>') + '</a>'
    return icons_html
#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

#def txt3(a, b):
  #col1, col2 = st.columns([1,2])
  #with col1:
    #st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  #with col2:
    # Split the text at the comma and wrap each part in backticks separately
    #b_parts = b.split(',')
    #b_formatted = '`' + ''.join(b_parts) + '`'
    #st.markdown(f'<p style="font-size: 20px; font-family: monospace;">{b_formatted}</p>', unsafe_allow_html=True)
    #st.markdown(f'<p style="font-size: 20px; color: red;"></code>{b}</code></p>', unsafe_allow_html=True)

def txt3(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  with col2:
    b_no_commas = b.replace(',', '')
    st.markdown(b_no_commas)

def txt4(a, b):
  col1, col2 = st.columns([1.5,2])
  with col1:
    st.markdown(f'<p style="font-size: 25px; color: white;">{a}</p>', unsafe_allow_html=True)
  with col2: #can't seem to change color besides green
    st.markdown(f'<p style="font-size: 25px; color: red;"><code>{b}</code></p>', unsafe_allow_html=True)

#####################

# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
#         background-size: cover
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
#     )
# add_bg_from_local('bg.png')   

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover;
            background-color: transparent;
            color: black;
        }}
        .stMarkdown {{
            color: black;
        }}
        .block-container {{
            background-color: transparent;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local('bg.png')


# # Sidebar: If using streamlit_option_menu
# with st.sidebar:
#     with st.container():
#         l, m, r = st.columns((1,3,1))
#         with l:
#             st.empty()
#         with m:
#             st.image(img_lh, width=175)
#         with r:
#             st.empty()
    
#     choose = option_menu(
#                         "Mustafa Mujahid", 
#                         ["About Me","Resume", "Experience", "Technical Skills", "Education", "Projects", "Competitions", "Volunteering", "Blog"],
#                          icons=['person fill', 'globe', 'clock history', 'tools', 'book half', 'clipboard', 'trophy fill', 'heart', 'pencil square', 'image', 'paperclip', 'star fill', 'envelope'],
#                          menu_icon="mortarboard", 
#                          default_index=0,
#                          styles={
#         "container": {"padding": "0!important", "background-color": "#f5f5dc"},
#         "icon": {"color": "darkorange", "font-size": "20px"}, 
#         "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#         "nav-link-selected": {"background-color": "#cfcfb4"},
#     }
#     )
#     #youtube_url = "https://www.youtube.com/@harrychangjr"
#     linkedin_url = "https://www.linkedin.com/in/mustafa-mujahid-0675a122b/"
#     #github_url = "https://github.com/harrychangjr"
#     medium_url = "https://medium.com/@mustafamujahid01"
#     email_url = "mailto:mustafamujahid01@gmail.com"
#     with st.container():
#         l, m, r = st.columns((0.11,2,0.1))
#         with l:
#             st.markdown("---")
#         with m:
#             st.markdown(
#                 social_icons(35, 35, LinkedIn=linkedin_url, Medium=medium_url, Email=email_url),
#                 unsafe_allow_html=True)
#         with r:
#             st.markdown("---")

# st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
# st.title("Mustafa Mujahid")

# Sidebar: If using streamlit_option_menu
with st.sidebar:
    with st.container():
        l, m, r = st.columns((1,3,1))
        with l:
            st.empty()
        with m:
            st.image(img_lh, width=175)
        with r:
            st.empty()
    
    choose = option_menu(
                        "Mustafa Mujahid",
                        ["About Me","Resume", "Experience", "Technical Skills", "Education", "Projects", "Competitions", "Volunteering", "Blog"],
                         icons=['person fill', 'globe', 'clock history', 'tools', 'book half', 'clipboard', 'trophy fill', 'heart', 'pencil square', 'image', 'paperclip', 'star fill', 'envelope'],
                         menu_icon="mortarboard", 
                         default_index=0,
                         styles={
        "container": {"padding": "0!important", "background-color": "#f5f5dc", "font-color": "black"},
        "options": {"color": "black", "font-size": "20px"},  # Adjusted style for the title
        "icon": {"color": "darkorange", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#eee", "color": "black"},
        "nav-link-selected": {"background-color": "#cfcfb4"},
        "menu-title": {"color": "black"}
    }
    )
    linkedin_url = "https://www.linkedin.com/in/mustafa-mujahid-0675a122b/"
    medium_url = "https://medium.com/@mustafamujahid01"
    email_url = "mailto:mustafamujahid01@gmail.com"
    with st.container():
        l, m, r = st.columns((0.11,2,0.1))
        with l:
            st.markdown("---")
        with m:
            st.markdown(
                social_icons(35, 35, LinkedIn=linkedin_url, Medium=medium_url, Email=email_url),
                unsafe_allow_html=True)
        with r:
            st.markdown("---")

st.write('<style>div.block-container{padding-top:0rem;color:black;}</style>', unsafe_allow_html=True)
st.title("Mustafa Mujahid")
# Create header
if choose == "About Me":
    #aboutme.createPage()
    with st.container():
        left_column, middle_column, right_column = st.columns((1,0.2,0.5))
        with left_column:
            st.header("About Me")
            st.subheader("Aspiring Deep Learning/Machine Learning Engineer")
            st.write("👋🏻 Hi, I'm Mustafa! I'm 23. I'm a Information technology undergraduate based in India. I am constantly seeking unique internships and full time roles to broaden my horizons on my Machine Learning or Deep Learning career.")
            st.write("💼 In this AI revolution, many groundbreaking researches are carried out and i am following them closely and practice them very often. In response to the increasing demand for AI candidates, I am thus aiming to enter this industry for my first full-time job.")
            st.write("🏋🏻 In addition, I like to write blogs, ride bikes, practice calisthenics, play table tennis and... enjoy eating and cooking good food in my free time!")
            st.write("𝌩 Strength: Quick Learner, Honesty, Creativity, Leadership, Writing skills, presenting skills, versatility")
            st.write("💭 Ideal Career Prospects: Machine Learning Engineer, Deep Learning Engineer, LLM Engineer, Data Analyst, Data Scientist, Data Engineer, Business Intelligence Analyst, Product Manager")
        with middle_column:
            st.empty()
        with right_column:
            st.image(img_utown)

# Create section for Work Experience
elif choose == "Experience":
    #st.write("---")
    st.header("Experience")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_hedgedrip)
        with text_column:
            st.subheader("Co-Founder & Technical Lead, HyperStyle Labs")
            st.write("*January 2024 to Present*")
            st.write("**Area:** IT & Services")
            st.markdown("""
            **🎯Purpose:** Deliver high quality Web & Mobile Applications, Cloud Services and other tech solutions to Businesses, Researchers and Outsourced Projects. 
            * **👨🏻‍💻My Role**
            - **System Design & Architecture:**
                - Conceptualize and develop scalable system architectures tailored to client requirements.
                - Select appropriate technologies and frameworks to ensure optimal performance and maintainability.
            - **Project Management & Team Leadership:**
                - Assemble the developers of required roles on a project basis to ensure the successful delivery of projects.
                - Implement agile methodologies to enhance team collaboration, productivity, and project transparency.
            - **Financial Management:** 
                -  Oversee financial aspects of projects, including budgeting, developer fee management, and lead generator fee allocation.
                -  Ensure transparent and accurate accounting practices to maintain financial health and client trust.
            - **Business Development & growth:**
                - Develop and maintain strong client relationships to drive repeat business and referrals.
                - Contribute to strategic planning and growth initiatives to expand the company’s market presence and service offerings.          
            `Project Management`, `Notion`, `Accounts`, `System Design` 
            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_groundup)
        with text_column:
            st.subheader("Data Science Intern, Tiranga Textiles")
            st.write("*August 2023 to March 2024*")
            st.write("**Area:** Data Science")
            st.markdown("""
            **🎯Purpose:** To bring change into tradtional information storing and retrieval process which is done using pen and paper to modern storage and analysis techniques.
            * **👨🏻‍💻My Role**
            - **Data Collection & Storage:**
                - Implemented efficient data collection processes to gather relevant production data from Google Forms.
            - **Data Pipeline Development:**
                - Developed and managed end-to-end data pipelines to streamline the flow of data from collection to analysis.                
            - **Data Visualization & Insights:** 
                -  Created dynamic dashboards and visualizations to present key insights and trends to textile firm owner.
            - **Machine Learning & Predictive Analytics:**
                - Built and deployed machine learning models to predict taka(cloth) production, improving production planning and resource allocation.
                - Integrated predictive algorithms into existing systems to provide real-time production forecasts.
            - **Performance Metrics & KPI Analysis:**
                - Developed and tracked key performance indicators (KPIs) to evaluate worker performance and productivity.
            
            `Python`, `Streamlit`, `Google Cloud Platform`, `SQL`, `Plotly`, `Numpy`, `Pandas`, `Scikit Learn`
            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_bitmetrix)
        with text_column:
            st.subheader("Quality Control Intern, Pneucon Valves")
            st.write("*June 2019 to August 2019*")
            st.write("**Area:** Mechnical Engineering")
            st.markdown("""
            **🎯Purpose:** To deliver best quality valves and thoroughly inspecting valves, bolts and mechanical functionalities before supplying.
            * **👨🏻‍💻My Role**
            - **Quality Assurance:** 
                - Implement and adhere to quality control processes to ensure the highest level of product quality.
                - Maintain accurate records of inspection results and quality assurance processes.
            - **Valve Inspection:**
                - Conducted comprehensive inspections of valves to ensure they meet quality standards and specifications.
            - **Mechanical Functionality Checks:**
                - Verify the mechanical functionalities of valves, ensuring optimal performance and reliability.
            
            `Machine Design`, `AutoCAD`, `Quality Control`, `Documentation` 
            """)
    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)
#st.write("##")

# Create section for Technical Skills

elif choose == "Technical Skills":
    #st.write("---")
    st.header("Technical Skills")
    def txtmust(title, skills):
        st.markdown(f"**{title}**: `{skills}`")
    txt3("Programming Languages"," `Python`, `C#`, `Java`,")
    txt3("Academic Interests","`Deep Learning`, `MLOps`, `Machine Learning`, `Data Science`")
    txt3("Data Visualization", "`Matplotlib`, `Seaborn`, `Plotly`")
    txt3("Database Systems", "Yet to Update")       #👨🏻‍💻TODO: Quickly learn any database systems and update the info here.
    txt3("Cloud Platforms", "`Amazon Web Services`, `Streamlit Cloud`, `Hugging Face`")
    txt3("Version Control", "`Git`, `MLFlow`")
    txt3("Design and Front-end Development", "`Canva`, `Figma`, `HTML`, `CSS`, `Streamlit`")
    txt3("Data Science Techniques", "`Regression`, `Clustering`, `Association Rules Mining`, `Random Forest`, `Decison Trees`, `Text Classification`, `Sentiment Analysis`, `Collaborative Filtering`")
    txt3("Machine Learning Frameworks", "`Numpy`, `Pandas`, `Scikit-Learn`, `TensorFlow`, `Keras`, `PyTorch`")
    txt3("Deep Learning Concepts", "`CNN`, `RNN`, `LSTM`, `LLM`, `Computer Vision`, `Transfer Learning`, `Fine Tuning`, `Reinforcement Learning`, `AI Ethics` ")
    txt3("Academic Concepts", "`Object Oriented Programming`, `Networking`, `System Design`, `Cloud Services`, `Big Data Technologies`")
    txt3("Task Management Tools", " `Notion`")
    txt3("Miscellaneous"," `Google Firebase`, `Microsoft Office`")

# Create section for Education
#st.write("---")
elif choose == "Education":
    st.header("Education")
    # selected_options = ["Summary", "Modules"
    #                     ]
    # selected = st.selectbox("Which section would you like to read?", options = selected_options)
    # st.write("Current selection:", selected)
    #if selected == "Summary":r
    st.write("*Summary of education from primary school till university*")
    with st.container():
        image_column, text_column = st.columns((1,2.5))
        with image_column:
            st.image(dmce)
        with text_column:
            st.subheader("Bachelor of Engineering - Information Technology, [Datta Meghe College of Engineering](https://www.dmce.ac.in/), [University of Mumbai](https://mu.ac.in/) (2020-2024)")
            st.write("Relevant Coursework: Data Structures & Algorithms, Computer Networks, Operating Systems, Wireless Technology, Data Science - I,Data Science - II, Database Management Systems, Software Engineering, Cryptograpy & Network Security, Cyber Security & Laws, Computer Organization & Architecture, Project Management, Big Data Analytics, Cloud Computing & Services,Web X, Object Oriented Programming, Blockchain Technology, Internet of Things")
            # st.markdown("""
            # - [NUS Product Club](https://linkedin.com/company/nusproductclub) - Co-founder & President (2023-24)
            # - [NUS Statistics and Data Science Society](https://sites.google.com/view/nussds/home) - President (2022), Marketing Director (2021-22)
            # - [Google Developer Student Clubs NUS](https://dsc.comp.nus.edu.sg/) - Deputy Head of Finance (2021-22)
            # """)
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(mumbai_uni)
            with text_column:
                st.subheader("Bachelor of Engineering (Honors) - Artificial Intelligence & Machine Learning (AIML), [University of Mumbai](https://mu.ac.in/) (2022-2024)")
                st.write("Coursework: Mathematics for AI & ML, Game Theory using AI & ML, AI & ML in Healthcare, Text Web & Social Media Analytics")
                st.markdown("""
                *This is a Mumbai University affiliated course in which selected students are supposed to complete this course along with their regular academic courses i.e (B.E in Information Technology) in my case.*
                """)
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(ssjp)
            with text_column:
                st.subheader("Diploma in Engineering - Mechanical Engineering, [Shivajirao S. Jondhle Polytechnic](https://www.jondhlepoly.org/), [Maharashtra State Board of Technical Education](https://msbte.org.in/) (2017-2020)")
                st.write("Coursework: Mathematics, Engineering Drawing, AutoCAD, Strength of Materials, Theory of Machines, Thermal Engineering, Fluid Mechanics & Machinery, Machine Design, Manufacturing Process, Mechanical Engineering Measurements")
                # st.markdown(""" 
                # - Track and Field - 100m (2016 A Division Semi-finalist), 200m, 4x100m
                # - TPJC Economics and Financial Literacy Fair 2015 - Games Facilitator
                # """)
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(national)
            with text_column:
                st.subheader("Primary & Secondary School - Dr. Omprakash Agarwal English High School (2005 - 2017)")
                st.write("Coursework: English, Mathematics, Science, History, Political Science, Geography, Marathi, Hindi")

elif choose == "Projects":
    # Create section for Projects
    #st.write("---")
    st.header("Projects")
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("XParse")
            st.write("*From Chaos to Clarity with GenAI*")
            st.markdown("""
            - Built an web application where users or businesses can upload pdf of multiple pages with unstrucutred data and application will convert that unstructured raw data into structured json or csv format.
            - By leveraging the power of open source LLMs the application refined, automated and optimized the way data is mined from raw into an organized format.
            - This work which usually takes hours when done manually is reduced by 90% by the use of GenAI.
            - In this project, i harness the power of Gemini 1.5 Pro and perform prompt tuning techniques to make it work with tabular data or paragraphs of words or invoice data.
            - Users can make on-the-go corrections if necessary. The application tracks all changes and displays the modifications, ensuring transparency and accuracy.
            *(Did you know: "This project got me and my team Rs 1,00,000/- cheque with trophy and a PPO.")*
            """)
            # st.write("[Github Repo](https://github.com/harrychangjr/sales-prediction)")
            #mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/blockchain-webscraping",)
        with image_column:
            st.image(images_projects[0])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("UrGPT")
            st.write("*Pushing the Boundaries of Language Models*")
            st.markdown("""
            - Developed a private GPT utilizing open-source LLMs for enhanced language processing capabilities.
            - Applied quantization techniques to optimize a 13 billion paramter model WizardLM-13B for efficient resource utilization
            - Implemented innovative features such as Document Question Answering, Coding Assistance, General QA enhancing the capabilities beyond what is offered in GPT 3.5.
            - Streamlined memory management in Buffer Memory, improving efficiency and overall system performance.
            - Ensured chat session continuity and context retention in memory for a seamless user experience.
            *(Did you know: "This project is developed during the Early days of LLMs")*
            """)
            # st.write("[Github Repo](https://github.com/harrychangjr/sales-prediction)")
            # mention(label="Streamlit App", icon="streamlit", url="https://huggingface.co/spaces/harrychangjr/tiktok_analytics",)
            # mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/tiktok-analytics",)
        with image_column:
            st.image(images_projects[1])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("FragAbs")
            st.write("*Making the abstracts easier to digest*")
            st.markdown("""
            - Developed a deep-learning model that classifies the abstract of the paper into BACKGROUND, OBJECTIVE, METHODS,RESULTS, and CONCLUSION.
            - This project was trained from scratch right from preprocessing the data to training the model to evaluating the results to deploying the model to HuggingFace Space.
            - During the later stages of this project, i applied fine tuning concept to make this model more accurate and refined. I used BERT model as a pretrined model. 
            - My team developed a user friendly UI for this project using React and Django and also mounted in-built dictionary onto the app so the users can understand the words on the go.
            - Saved the weights of the model in the .h5 format which was used in backend for prediction.
            *(Did you know: “This has to be my first major project, which I built from scratch and for which I earned several awards and certificates.”)*
            """)
        
        with image_column:
            st.image(images_projects[2])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Data Fabric")
            st.write("*Weaving Analytics for Textile Excellence*")
            st.markdown("""
            - Designed a dashboard using Streamlit and built the data pipelines which ingest the data from the user through google forms to google spreadsheet and spreadsheet was connected to the dashboard which fuels up the dashboard with the data.
            - This project was made to solve the problems of Textile firms owners who were facing data storing and retrieval problems along with no use of data.
            - Performed various data analytics operations to visualize the insights from the data.
            - Displayed useful information such as daily production, worker performance in a highlight format using Key Performance Indicators.
            - Hosted Machine Learning in the application which predicts the production of the cloth for the next month & quarter.
            *(Did you know: "This was my project during my tenure at Tiranga Textile as an Intern.")*
            """)
            
        with image_column:
            st.image(images_projects[3])
    with st.container():
        text_column, image_column = st.columns((3,1))
        with text_column:
            st.subheader("Carvana Image Masking")
            #st.write("*Completed project within 48 hours for module ST4248: Statistical Learning II in Academic Year 2022/23 Semester 2*")
            #st.write("Methods performed on [Kaggle dataset](https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings):")
            st.markdown("""
            - Developed a deep learning model using the U-Net architecture to perform image segmentation on the Carvana Image Masking Challenge dataset. 
            - Implemented data augmentation techniques, mixed precision training to increase performance and reduce training time.
            - Converted the predicted masks into the run-length encoded format required for submission and submitted the results on Kaggle.
            *(Did you know: "This project was made by me for competing in the competition which was hosted by the Carvana Company on the Kaggle platform.")*
            """)
            
        with image_column:
            st.image(images_projects[4])
    
elif choose == "Competitions":
    # Create section for Competitions
    #st.write("---")
    st.header("Competitions")
    st.markdown("*Project name of project is mentioned which was developed during the competition. Detials of the project developed is present in the Projects section of this website.*")
    
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(logithon)
            #st.empty()
        with text_column:
            st.subheader("[LogiTHON Hackathon](https://www.logithon.ai/) - Hosted by in collaboration of [DMCE](https://www.dmce.ac.in/) & [Softlink Global](https://softlinkglobal.com/)")
            st.markdown("""
            - Rank - 1st
            - Project Name - XParse
            - Team Name - DataMiners
            - Problem Statement - 4
            - Team Members - [Hrushabh Patade](https://www.linkedin.com/in/hrushabh-patade/) [Janhavi Chaudhari](https://www.linkedin.com/in/janhavi-chaudhari-a6a832247/) [Ganesh Padval](https://www.linkedin.com/in/ganesh-padval/)
            """)
            mention(label="Company's Blog", url="https://softlinkglobal.com/logithon-to-recreate-the-future-of-logistics-industry/",); mention(label="Organizers Blog", url="https://logithon.wordpress.com/2024/04/22/logithon-signing-off-%f0%9f%91%8b/",)
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(dmce_hackathon)
            #st.empty()
        with text_column:
            st.subheader("[DMCE Hackathon 2.0](https://gits-hackathon24.vercel.app/hackathon24) - Hosted by [GITS DMCE](https://gits-hackathon24.vercel.app/)")
            st.markdown("""
            - Rank - 2nd
            - Project Name - UrGPT
            - Team Name - Humanoids
            - Problem Statement - Student Innovation
            - Team Members  - [Aarish Khan](https://www.linkedin.com/in/aarish-khan-7b66481bb/) [Ashlesha Waghambare](https://www.linkedin.com/in/ashlesha-waghambare-88b09925b)
            """)
           
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(prakalp_2k23)
        with text_column:
            st.subheader("[Prakalp 2k23](https://unstop.com/competitions/prakalp-2k23-fr-conceicao-rodrigues-college-of-engineering-frcrce-mumbai-611100) - Hosted by [Fr. Conceição Rodrigues College of Engineering](http://www.frcrce.ac.in/)")
            st.markdown("""
            - Rank - 3rd
            - Project Name - FragAbs
            - Team Name - Humanoids
            - Problem Statement - Software Category
            - Team Members  - [Usama Ansari](https://www.linkedin.com/in/mohd-usama-ansari-13b06421b/) [Ganesh Padval](https://www.linkedin.com/in/ganesh-padval/) [Hrushabh Patade](https://www.linkedin.com/in/hrushabh-patade/)
            """)
            
            
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(alice)
        with text_column:
            st.subheader("Alice in Borderland - Hosted by [GITS DMCE](https://gits-hackathon24.vercel.app/)")
            st.write("This was a coding quest taken place in college cultural event.")
            st.markdown("""
            - Rank - 2nd
            - Team Name - We are Heroes
            - Team Members  - [Adhyatm Mishra](https://www.linkedin.com/in/adhyatma-mishra-b51370227/) 
            """)
            
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(rd_national)
        with text_column:
            st.subheader("[SynTech-X Hackathon](https://unstop.com/hackathons/syntech-x-hackathon-syntech-x-rd-national-154728) - Hosted by [RD National College](https://rdnational.ac.in/)")
            st.markdown("""
            - Rank - Runner Up
            - Project Name - FragAbs
            - Team Name - Humanoids
            - Problem Statement - Student Innovation
            - Team Members  - [Usama Ansari](https://www.linkedin.com/in/mohd-usama-ansari-13b06421b/) [Ganesh Padval](https://www.linkedin.com/in/ganesh-padval/) [Hrushabh Patade](https://www.linkedin.com/in/hrushabh-patade/)
            """)
            
elif choose == "Volunteering":
    st.header("Volunteering")
    with st.container():
        text_column, mid, image_column = st.columns((3,0.4,1))
        with text_column:
            st.subheader("Google Developer Student Clubs DMCE")
            st.write("*September 2022 to May 2023*")
            st.markdown("""
            **Technical Member**
            - Regulate news of upcoming sessions by GDSC to students and promote the events along with technical work.
            - Teamed with 4 other talented individuals and formed a GDSC DMCE AIML team which focuses on arranging workshops and seminars on Artificial Intelligence and Deep Learning.
            - Organised weekly sessions, events, hackathons and carried out many other educational and research activites.
            """)
        with mid:
            st.empty()
        with image_column:
            st.image(images_vol[0])
    with st.container():
        text_column, mid, image_column = st.columns((3,0.4,1))
        with text_column:
            st.subheader("Smart India Hackathon")
            st.markdown("""
            **Volunteer** (*This responsibility ignites the spark in me of going to hackathons.*)
            - Volunteered in Smart India Hackathon which is a National Hackathon comprise of teams from different states showcasing their projects. 
            - Worked as a assistance to participants of the hackathon. This activity includes solving their queries regarding event, lab assist, providing meals & maintain decorum.
            """)
        with mid:
            st.empty()
        with image_column:
            st.image(images_vol[1])
    
    
elif choose == "Blog":
    st.write("Click two times on Read More button to react.")
    # Sample data for blog posts
    blogs = [
        {
            "title": "LogiTHON: My Biggest Win of all Time!!",
            "date": "April 24 2024",
            "image": "image_collection/blog/og.jpg",
            "content": """
            In the month of March 2024, when I was worried about the final exams, vivas, submissions which was commencing from 24 April. A news about LogiTHON spread like a wildfire in our institute. Everyone around me was talking about it. I came to know that it was just a hackathon and I at that time was not personally interested to take part in it. But the reward of winning the hackathon caught my eye. A prize pool of 6 lakhs rupees and not just that a winner will also get a Pre placement offer for Softlink global a logistics company who was also organizing the event. But still wasn’t sure to take part  in it as it is scheduled right before my exams. But my friends later my team members somehow convinced me to take part. I also thought what a best way to end my college life. I started winning hackathons from runner up to  third to second but never won first place. Let’s take a shot. So, we DataMiners a group of 4 people participated in the event. The Competition consists of three stages . Every stage was an elimination round. In first round, the team has to submit  a ppt along with a video explanation of how we are going to approach & solve the problem. So I took the charge of it from my team and we submitted the video. And something funny happened that I wish I can reveal. Overall, we got selected in the first round. We got very happy hearing news that we got selected and also shocked that there were 1500+ participants and 565 teams in total who participated for this hackathon. After filtering out from the round1 , 60 teams left for 4 problem statements. And we all were waiting excitedly for the event day which was on 19th April. 


**First Day (19 April)**

As always I reached the location 1.5 hours late registered at the counter took my ID, T-shirt and other goodies & then attended the pre-event talks, understand rules and event timelines. This was a 48 hours hackathon and i never experienced such long event before in my life. Then we were assisted towards the lab and we without wasting a minute  got started working on our project. 

First day that was on Friday spent well me and my team discussed a lot, coded a lot and designed a lot. Thoughtout this day we enjoyed delicious breakfast, lunch and dinner. Have to applaud for the organising team and volunteers they managed everything  so well. At midnight we got to experience the jamming session which really helped our mind to relax and refresh. But just sitting half an hour we headed back to the lab worrying about the next final day. Around 2.30 AM in the night we were told to had snacks. They served Maggi(Noodles) as a midnight snack. I swear that’s the worst Maggi I ever ate. 3 years old without bun burger >>>> that Maggi. So. I took back all the kind words I said about the organisers. Just Kidding. But yeah that maggi part was true. At 4.00 AM in the night we were walking in the college lobby and clicking photos for absolutely no reason. Then at 5.00 AM i got to sleep. I woke up at 7.30 AM and saw 7 missed calls from my team members I called them back and they said round 2 is about to begin. I rushed to the lab and made my pitching script.


**D-Day**

The judges came and I was prepared to elaborate my script which I rehearsed for like 1000 times. But the judging round didn’t go as planned. The judging session becomes so raw that we had such a healthy conversation about and apart from the project. That discussion showed as the clear signs of getting selected for round 3. 

Later, waiting for about 2 hours for results of next round we got to know from volunteers whoever got the call from the organisers are selected for round 3. We waited. Waited for 20 minutes and didn’t got any call. We were upset. We packed our bags got in the lift and about to leave the institute. Then my team leader got a call we became very excited that maybe it was the call from the organizers but it was his father and we were upset again. We saw the expression of our team leader he seemed quite happy and we curiously asked him that what happened he replied during registration process his phone number was unavailable so he registered using his father’s phone number. So that’s why his father called and said to him “You fool where have you gave my number someone called me and said Congratulations your team is selected come to seminar hall for the final round. Don’t you dare give my phone number to anyone” and hung up the call. We burst out in laughter and got a relief that we were selected for the round 3. 

**Final Round**

Now from total 60 teams of all four problem statements only 16 teams made it to the final round i.e 4 teams from each problem statement. For each p.s, among 4 teams, 1 team will be winner and 1 team will be runner up defeating the other two teams. 

In round 3, for the very first time I had to address such a big crowd from the stage on the mic. CEO of Softlink Global, Judges, Chief guests, Principal, teaching staff, participants, organizers, volunteers and students everyone was present in the audience. 

I got so nervous that I almost started shivering maybe my gut was not feeling well or maybe that Maggi is showing its true colours so before our presentation I gone to washroom stick two fingers in my throat and vomitted. I then washed my face looked in the mirror and said “You’ve already won, just one more round”. Now as my steps was reaching towards the backstage for presentation *my heart was beating like a drum*. I reached backstage, revised my lines, made dua for success and step on the stage leaving my fear and anxiety idle on the backstage. 

I stood, delivered, answered and left. Gone out the seminar hall drank a lot of water and took a deep breath and said to myself “You did your best”. After everyone’s presentation judges discussed and decided the winners.

**Result Time**

At 8.00 PM they started announcing the results. We were in the last problem statement category. i.e ps4. They started announcing results from ps1 in a format of first disclosing the runner up and then the winner. ps1 results announced, ps2 results announced followed by ps3. Now time for our ps i.e ps4. At that moment, we were praying for the runner up position because all the other contestants were also so good that we are limiting our chances of winning the first prize and we were *aiming lower and settling for the minimum.* 


The Speaker announcing the result said “Now for the 4th problem statement runner up goes to ………..” some other team. We lost hope and taken back seat. After giving the prize to runner up speaker once again came up to stage and said “Now time for the last award of this long night and long 48 hour massive logithon event. The first prize for the problem statement 4 goes to……any guesses……no…..goes to Team DataMiners from Datta Meghe College of Engineering
”. I held my head high stood up and in shock thinking what just happened. Everything in my mind was started happening in slow motion , surrounding noise drops to very low and heart again started beating but this time *beating like a violin*. People around us stood up clapping loudly, whistling, cheering as we make our way upto the stage. We received the cheque, grabbed the trophy and lifted it up high and smiled towards the camera thinking always *aim higher and never settle for the minimum.* I then had good 20-25 mins discussion with the manager of the softlink global and the important takeaway I got from him is **“Tomorrow put this victory in the back view mirror of your career and start working towards your next goal.” ** Everyone in my team was calling their parents conveying the good news. But I somehow resisted myself from calling my parents as I wanted to tell them in person.


**Farewell**

We, Collected our certificates and gift hamper and left the college. We felt so fun taking that 1 lakh rupees cheque from the college towards the railway station protecting it from any obstacles like it was now a part of us. I then gone home showed my Mum the certificates, awards, gift hamper, photos and she replied as like every other Universal dialogue of every mother “Have you ate properly throughout the competition?” 

I then washed my face and requested my mum to give me a head massage. And I slept. Slept for 10 long hours and woke up next morning, replied Thank you to everyone’s messages and started preparing for my exams. 

When I started my college life i volunteered at a SIH hackathon. As a volunteer, I got the opportunity to look at the participants projects, their presentations, team efforts and while providing them their meals I decided that one day I will also be a participant of such a big national hackathon event and I will win it.

And the rest is history. 

    """,
            "url": None
        },
  
        {
            "title": "My First Blog",
            "date": "6 August 2023",
            "image": "image_collection/blog/medium.jpg",
            "content": "",
            "url": "https://medium.com/@mustafamujahid01/pytorch-for-mac-m1-m2-with-gpu-acceleration-2023-jupyter-and-vs-code-setup-for-pytorch-included-100c0d0acfe2"
        }
    ]


    #Function to display a blog card
    # def display_blog_card(blog, index):
    #     with st.container():
    #         cols = st.columns([2, 1])
    #         with cols[0]:
    #             st.markdown(f"### {blog['title']}")
    #             st.markdown(f"*{blog['date']}*")
    #             if blog['url']:
    #                 if st.button(f"Read More", key=f"btn_{index}"):
    #                     st.session_state.selected_blog_url = blog['url']
    #             else:
    #                 # Use a unique key for each button to prevent multiple clicks
    #                 if st.button(f"Read more", key=f"read_more_{index}"):
    #                     st.session_state.selected_blog = index
    #         with cols[1]:
    #             st.image(blog['image'], use_column_width=True)
    #         st.markdown("---")  # Separator

    # # Check if a blog is selected
    # if "selected_blog" not in st.session_state:
    #     st.session_state.selected_blog = None

    # if "selected_blog_url" not in st.session_state:
    #     st.session_state.selected_blog_url = None

    # # Display blog cards or selected blog content
    # if st.session_state.selected_blog is None and st.session_state.selected_blog_url is None:
    #     for i, blog in enumerate(blogs):
    #         display_blog_card(blog, i)
    # else:
    #     if st.session_state.selected_blog_url:
    #         # Redirect to external blog URL
    #         st.write(f"Redirecting to [this blog]({st.session_state.selected_blog_url})...")
    #         st.markdown(f'<meta http-equiv="refresh" content="0; url={st.session_state.selected_blog_url}">', unsafe_allow_html=True)
    #     else:
    #         # Display selected local blog content
    #         selected_blog = blogs[st.session_state.selected_blog]
    #         st.image(selected_blog['image'], use_column_width=True)
    #         st.markdown(f"### {selected_blog['title']}")
    #         st.markdown(f"{selected_blog['date']}")
    #         st.write(selected_blog['content'])
            
    #         if st.button("Back to Blog Posts"):
    #             st.session_state.selected_blog = None
    #             st.session_state.selected_blog_url = None

    # Function to display each blog card
    def display_blog_card(blog, index):
        with st.container():
            cols = st.columns([2, 1])
            with cols[0]:
                st.markdown(f"### {blog['title']}")
                st.markdown(f"*{blog['date']}*")
                if blog['url']:
                    if st.button(f"Read More", key=f"btn_{index}"):
                        st.session_state.selected_blog_url = blog['url']
                else:
                    if st.button(f"Read More", key=f"read_more_{index}"):
                        st.session_state.selected_blog = index
            with cols[1]:
                st.image(blog['image'], use_column_width=True)
            st.markdown('<hr style="border: 0.5px solid #030300;">', unsafe_allow_html=True)  # Separator

    # Initial session state
    if "selected_blog" not in st.session_state:
        st.session_state.selected_blog = None

    if "selected_blog_url" not in st.session_state:
        st.session_state.selected_blog_url = None

    # Display blog cards or selected blog content
    if st.session_state.selected_blog is None and st.session_state.selected_blog_url is None:
        for i, blog in enumerate(blogs):
            display_blog_card(blog, i)
    else:
        if st.session_state.selected_blog_url:
            st.write(f"Redirecting to [this blog]({st.session_state.selected_blog_url})...")
            st.markdown(f'<meta http-equiv="refresh" content="0; url={st.session_state.selected_blog_url}">', unsafe_allow_html=True)
        else:
            selected_blog = blogs[st.session_state.selected_blog]
            st.image(selected_blog['image'], use_column_width=True)
            st.markdown(f"### {selected_blog['title']}")
            st.markdown(f"{selected_blog['date']}")
            st.write(selected_blog['content'])
            
            if st.button("Back to Blog Posts"):
                st.session_state.selected_blog = None
                st.session_state.selected_blog_url = None

elif choose == "Resume":   
    resume_url = "https://drive.google.com/file/d/1AbBQRwfqEAbSS7-4bc4zVNRdgLJmpgHC/view?usp=sharing"
    st.header("Resume")
    st.write("*In case your current browser cannot display the PDF documents, do refer to the hyperlink below!*")

    st.markdown(pdf_link(resume_url, "**Resume (1 page)**"), unsafe_allow_html=True)
    show_pdf("Resume.pdf")
    styled_download_button("Download Resume (1 page)", "Resume.pdf")
