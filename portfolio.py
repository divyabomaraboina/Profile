import streamlit as st
import base64


# --------------------------
# Page Configuration
# --------------------------
st.set_page_config(
    page_title="Divya Bomaraboina | Data Science Portfolio",
    layout="wide",
    page_icon="📊",
    initial_sidebar_state="expanded"
)


# --------------------------

# Custom CSS Styling with Animations
# --------------------------
st.markdown("""
<style>
    :root {
        --primary: #2B3A55;
        --secondary: #3F72AF;
        --accent: #FF7C7C;
        --background: #F9F7F7;
    }
    
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    
    .header {
        color: var(--primary);
        padding: 1rem 0;
        font-size: 2.8rem;
        animation: fadeIn 1s ease-in;
    }
    
    .project-card {
        transition: all 0.3s ease;
        cursor: pointer;
        border-left: 4px solid var(--secondary);
    }
    
    .project-card:hover {
        transform: translateX(10px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .tech-pill {
        display: inline-block;
        padding: 0.5rem 1.2rem;
        margin: 0.4rem;
        border-radius: 20px;
        background: var(--background);
        color: var(--primary);
        border: 1px solid var(--secondary);
        transition: all 0.3s ease;
    }
    
    .tech-pill:hover {
        transform: scale(1.05);
        background: var(--secondary);
        color: white;
    }
    
    .animated-button {
        transition: all 0.3s ease;
        border: 2px solid var(--secondary);
        position: relative;
        overflow: hidden;
    }
    
    .animated-button:hover {
        background: var(--secondary);
        color: white !important;
        transform: translateY(-2px);
    }
    
    .section-header {
        color: var(--secondary);
        border-bottom: 2px solid var(--accent);
        padding-bottom: 0.5rem;
        margin: 2rem 0;
    }
    
    .hover-zoom {
        transition: transform 0.3s ease;
    }
    
    .hover-zoom:hover {
        transform: scale(1.03);
    }
</style>
""", unsafe_allow_html=True)

# --------------------------
# Data Initialization
# -------------------------- 
# [Keep your existing projects data structure]

# --------------------------
# Header Section with Animation
# --------------------------
col1, col2 = st.columns([1, 3])

with col1:
    st.image(r"p1.jpg", width=300)
    st.markdown("""
    <div class="hover-zoom">
    <img src="https://via.placeholder.com/300" width="300" style="border-radius: 15px">
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="animation: fadeIn 1s ease-in">
    <h1 class="header">Divya Bomaraboina</h1>
    <h2 style="color: var(--secondary)">📚 Masters Student | 🔍 Data Enthusiast | ⚙️ Former Test Engineer</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.download_button(
        label="📄 Download Full Resume",
        data=base64.b64encode(open("https://drive.google.com/file/d/1s1JOf2JrfWRPSk6MmXifpWzQRGcNxQyo/view?usp=drive_link", "rb").read()),
        file_name="Divya_Bomaraboina_Resume.pdf",
        mime="application/octet-stream",
        use_container_width=True,
        key="resume-btn"
    )
    

# --------------------------
# Animated About Section
# --------------------------
st.markdown("""
<div class="section-header" style="animation: fadeIn 1s ease-in">
<h2>About Me</h2>
</div>
<div style="padding: 2rem; background: var(--background); border-radius: 10px; animation: fadeIn 1.2s ease-in">
<p style="font-size: 1.1rem; line-height: 1.6">
🌟 Currently pursuing my <strong>Master's in Analytics</strong> at Northeastern University with a 3.8 GPA<br>
🌐 Transitioned from Electronics Engineering to Data Science<br>
🔧 1+ years experience in automation engineering at Infosys<br>
📈 Specialized in predictive modeling and data storytelling<br>
🎨 Passionate about transforming raw data into visual narratives
</p>
</div>
""", unsafe_allow_html=True)
# In your About Section code, replace the buttons div with:
st.markdown("""
<div style="margin-top: 2rem; display: flex; gap: 1rem">
    <a href="https://medium.com/@divya.bomaraboina22" target="_blank" style="text-decoration: none">
        <button class="animated-button" style="padding: 0.8rem 1.5rem; border-radius: 8px">
            📚 Explore My Blogs
        </button>
    </a>
    <a href="https://www.linkedin.com/in/divyabomaraboina/details/certifications/" target="_blank" style="text-decoration: none">
        <button class="animated-button" style="padding: 0.8rem 1.5rem; border-radius: 8px">
            📄 View Certifications
        </button>
    </a>
</div>
""", unsafe_allow_html=True)


# --------------------------
# Interactive Project Showcase
# --------------------------
# --------------------------
# Data Initialization
# --------------------------
projects = {
    "AI-Driven Predictive PM Tool": {
        "description": "Advanced project management solution with 85% forecasting accuracy",
        "tech": ["Python", "TensorFlow", "Tableau", "Fast API"],
        "achievements": [
            "40% faster response time through chatbot automation",
            "25% improved risk assessment with AI detection",
            "70% automated project updates via interactive dashboard"
        ],
        "code":"https://github.com/divyabomaraboina/traxidy",
        "video": r"https://youtu.be/pnpyImGL2b0"
    },
    "Celebrity Search Application": {
        "description": "AI-powered information system using LangChain and OpenAI",
        "tech": ["LangChain", "OpenAI API", "Streamlit", "NLP"],
        "achievements": [
            "Integrated real-time data retrieval from multiple sources",
            "Implemented conversational memory for context-aware searches",
            "Developed interactive timeline of historical events"
        ],
        "code": "https://github.com/divyabomaraboina/Celebrity-Search-App",
        "video": r"https://youtu.be/c7i3M4Tq2cg"
    },
    "Restaurant Name Generator": {
        "description": "AI-driven culinary brand ideation system",
        "tech": ["LangChain", "LLMs", "Streamlit", "NLP"],
        "achievements": [
            "Multi-cuisine name generation with menu suggestions",
            "Integrated food trend analysis engine",
            "Dynamic output formatting for easy implementation"
        ],
        
        "video": r"https://youtu.be/3uR37nWmVDY"
    },
    "COVID-19 Predictive Analysis": {
        "description": "Mortality trend prediction with 85% accuracy using LSTM",
        "tech": ["Python", "LSTM", "Plotly", "CDC Data"],
        "achievements": [
            "Analyzed 137,700+ CDC records",
            "Identified high-risk elderly demographics",
            "30% faster analysis through team collaboration"
        ],
        "video": r"https://youtu.be/-tNd_tso1RI"
    },
    "Hospitality Data Analysis Dashboard": {
        "description": "Power BI dashboard for hotel occupancy and revenue insights",
        "tech": ["Power BI", "Power Query", "DAX", "Data Modeling"],
        "achievements": [
            "Consolidated multiple CSV files into unified pipeline",
            "Redefined 'day_type' metrics using calculated fields",
            "Created interactive filters for real-time decision making"
        ],
        "video": r"https://youtu.be/lrHCk_TBBRs"
    },
    "NYPD Arrest Data Analysis": {
        "description": "Crime pattern analysis using statistical modeling",
        "tech": ["R", "Tableau", "Chi-Square", "ANOVA"],
        "achievements": [
            "Identified enforcement disparities through statistical analysis",
            "Created interactive arrest pattern visualizations",
            "Developed policy recommendations dashboard"
        ],
        "video": r"https://youtu.be/jS1ejEIkVaQ"
    }
}

# --------------------------
# Header Section
# --------------------------


# --------------------------


# --------------------------
# Project Showcase
# --------------------------
st.header("List of Projects", divider="blue")
selected_project = st.selectbox("Select a Project:", list(projects.keys()))

if selected_project:
    proj_data = projects[selected_project]
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"### {selected_project}")
        st.markdown(f"**{proj_data['description']}**")
        st.markdown("#### Key Achievements:")
        for achievement in proj_data['achievements']:
            st.markdown(f"<div class='achievement-bullet'>✅ {achievement}</div>", unsafe_allow_html=True)
        
        tech_display = " ".join([f"<span class='tech-pill'>{tech}</span>" for tech in proj_data['tech']])
        st.markdown(f"<div style='margin-top:1rem'>**Tech Stack:** {tech_display}</div>", unsafe_allow_html=True)
        
    with col2:
        if 'video' in proj_data:
            st.video(proj_data['video'])
        if 'code' in proj_data:
            st.markdown(f"""
            [![GitHub](https://img.shields.io/badge/View_Code-181717?style=for-the-badge&logo=github&logoColor=white)]({proj_data['code']})
            """)

# --------------------------
# Professional Experience
# --------------------------
st.header("Professional Journey", divider="orange")
with st.expander("### 💼 Infosys | Test Engineer (Nov 2022 - Nov 2023)"):
    st.markdown("""
    - Automated 40% of testing processes using Selenium frameworks
    - Reduced data inconsistencies by 20% through validation checks
    - Streamlined ETL processes for banking data transformation
    - Mentored 3 junior engineers in automation best practices
    """)

# --------------------------
# Skills Matrix
# --------------------------
st.header("Technical Expertise", divider="green")
skill_cols = st.columns(4)
skills = {
    "🤖 AI/ML": ["LangChain", "LLMs", "TensorFlow", "XGBoost"],
    "📊 Visualization": ["Tableau", "Power BI", "Plotly", "Streamlit"],
    "⚙️ Automation": ["Selenium", "Fast API", "REST API", "ETL"],
    "📈 Analytics": ["Python", "R", "SQL", "Statistical Modeling"]
}

for i, (category, items) in enumerate(skills.items()):
    with skill_cols[i]:
        st.markdown(f"#### {category}")
        for item in items:
            st.markdown(f"<div class='tech-pill'>{item}</div>", unsafe_allow_html=True)

# --------------------------
# Contact Section
# --------------------------
st.header("Let's Connect", divider="violet")
contact_cols = st.columns(3)
contact_cols[0].markdown("""
**Professional Links**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/divyabomaraboina)  
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/divyabomaraboina)
""")

contact_cols[1].markdown("""
**Collaboration Tools**  
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:bomaraboina.d@northeastern.edu)  
""")

# --------------------------
# Footer
# --------------------------
