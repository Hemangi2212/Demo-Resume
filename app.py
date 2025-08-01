import streamlit as st
from pathlib import Path

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Hemangi Ransing | Web Developer & Data Analyst",
    page_icon="👩‍💻",
    layout="centered"
)

# --- HEADER ---
st.title("👩‍💻 Hemangi Ransing")
st.subheader("Aspiring Web Developer & Data Analyst")
st.markdown("""
Hello! I'm Hema, a passionate fresher with hands-on experience in **Python**, **Web Development**, and **Data Analytics**.  
I love building websites and analyzing data to solve real-world problems.
""")

# --- ABOUT ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("## 🎯 About Me")
st.markdown("""
I'm a motivated computer science graduate with a strong foundation in programming and data analysis.  
Eager to contribute to impactful projects and grow as a full-stack developer and data professional.  
Currently exploring opportunities in web development, data science, and automation.
""")

# --- EDUCATION ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("## 🎓 Education")

col1, col2 = st.columns([2, 3])
with col1:
    st.markdown("**B.Tech. Computer Science**")
with col2:
    st.markdown("MIT AOE Pune | 2022 – 2025")

# Internships
st.markdown("### Internships")
st.write("- **Web Development Intern** – Built responsive websites using HTML, CSS, JavaScript")
st.write("- **Data Analytics Intern** – Analyzed datasets using Python, Pandas, and Power BI")

# --- SKILLS ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("## 🛠️ Skills")

# Organize skills in columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Programming & Web")
    st.write("- Python")
    st.write("- HTML/CSS/JavaScript")
    st.write("- Streamlit")
    
with col2:
    st.markdown("#### Data & Analytics")
    st.write("- Pandas, NumPy, Matplotlib")
    st.write("- SQL, Excel")
    st.write("- Power BI")

# --- PROJECTS (Optional - You can add later) ---
# st.markdown("<hr>", unsafe_allow_html=True)
# st.markdown("## 💼 Projects")
# st.write("Check out my [GitHub](https://github.com/yourgithub) for projects!")

# --- RESUME DOWNLOAD ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("## 📄 Resume")

# Check if resume file exists
resume_path = "Hema_Resume.pdf"
if Path(resume_path).exists():
    with open(resume_path, "rb") as file:
        btn = st.download_button(
            label="📥 Download My Resume (PDF)",
            data=file,
            file_name="Personal  Resume.pdf",
            mime="application/pdf"
        )
else:
    st.warning("Resume file not found. Please ensure `Hema_Resume.pdf` is in the same directory.")

# --- CONTACT ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("## 📬 Contact Me")

contact_info = """
- 📧 **Email:** ransinghemangi@gmail.com
- 💼 **LinkedIn:** [linkedin.com/in/yourprofile](www.linkedin.com/in/hemangi-ransing)  
- 🖥️ **GitHub:** [github.com/yourgithub](https://github.com/yourgithub)  
"""
st.markdown(contact_info)

# --- FOOTER ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<center style='color: gray;'>Built with ❤️ using Streamlit</center>", unsafe_allow_html=True)
