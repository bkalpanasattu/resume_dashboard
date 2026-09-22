import streamlit as st
import streamlit.components.v1 as components

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="Dr. Kalpana B - Executive Resume Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR STYLING & TOP-RIGHT PICTURE ---
st.markdown("""
<style>
    /* Global font & background enhancements */
    .main {
        background-color: #f8fafc;
    }
    .stAppHeader {
        background-color: rgba(255, 255, 255, 0.8);
    }
    
    /* Header Container styling */
    .header-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        color: white;
        padding: 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
        position: relative;
    }
    
    /* Profile Image Container at Top Right */
    .profile-img-container {
        float: right;
        margin-left: 20px;
        margin-bottom: 10px;
        text-align: center;
    }
    .profile-img {
        width: 140px;
        height: 140px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #38bdf8;
        box-shadow: 0 4px 12px rgba(56, 189, 248, 0.3);
        transition: transform 0.3s ease;
    }
    .profile-img:hover {
        transform: scale(1.05);
    }
    
    /* Subheading Cards with Pop-out / Expandable feel */
    .subheading-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-left: 5px solid #2563eb;
        padding: 1rem 1.25rem;
        border-radius: 10px;
        margin-bottom: 0.75rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        transition: all 0.2s ease-in-out;
    }
    .subheading-card:hover {
        box-shadow: 0 8px 16px rgba(37, 99, 235, 0.12);
        transform: translateY(-2px);
    }
    
    /* Badge styling */
    .badge {
        display: inline-block;
        background-color: #eff6ff;
        color: #1d4ed8;
        font-weight: 600;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.85rem;
        border: 1px solid #bfdbfe;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    .badge-gold {
        background-color: #fefce8;
        color: #a16207;
        border-color: #fef08a;
    }
</style>
""", unsafe_allow_html=True)

# --- MINIMALIST FLY CURSOR ANIMATION (JS INJECTION) ---
# Embeds a subtle fly cursor that smoothly follows mouse movements using HTML5 canvas/floating element
components.html("""
<style>
    #minimalist-fly {
        position: fixed;
        top: 0;
        left: 0;
        width: 24px;
        height: 24px;
        pointer-events: none;
        z-index: 999999;
        transition: transform 0.05s linear;
        display: flex;
        align-items: center;
        justify-content: center;
        filter: drop-shadow(0px 2px 4px rgba(0,0,0,0.3));
    }
    .fly-wing {
        animation: flap 0.1s infinite alternate ease-in-out;
    }
    @keyframes flap {
        0% { transform: scaleY(1); }
        100% { transform: scaleY(0.3); }
    }
</style>

<div id="minimalist-fly">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Fly Body -->
        <ellipse cx="12" cy="14" rx="4" ry="6" fill="#1e293b" />
        <circle cx="12" cy="7" r="3" fill="#0f172a" />
        <!-- Eyes -->
        <circle cx="10.5" cy="6" r="1" fill="#ef4444" />
        <circle cx="13.5" cy="6" r="1" fill="#ef4444" />
        <!-- Wings with flap animation -->
        <g class="fly-wing">
            <ellipse cx="7" cy="11" rx="5" ry="2.5" fill="rgba(148, 163, 184, 0.7)" transform="rotate(-25 7 11)" />
            <ellipse cx="17" cy="11" rx="5" ry="2.5" fill="rgba(148, 163, 184, 0.7)" transform="rotate(25 17 11)" />
        </g>
    </svg>
</div>

<script>
    const fly = document.getElementById('minimalist-fly');
    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let flyX = mouseX;
    let flyY = mouseY;

    window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });

    function animateFly() {
        // Smooth lerp (linear interpolation) follow
        const dx = mouseX - flyX;
        const dy = mouseY - flyY;
        
        flyX += dx * 0.15;
        flyY += dy * 0.15;
        
        // Calculate angle facing cursor direction
        const angle = Math.atan2(dy, dx) * (180 / Math.PI) + 90;
        
        fly.style.transform = `translate3d(${flyX - 12}px, ${flyY - 12}px, 0) rotate(${angle}deg)`;
        requestAnimationFrame(animateFly);
    }
    animateFly();
</script>
""", height=0, width=0)

# --- HEADER SECTION WITH TOP-RIGHT PICTURE ---
col_head1, col_head2 = st.columns([3, 1])

with col_head1:
    st.title("Dr. Kalpana B")
    st.caption("🏆 Gold Medalist | Rank 1 Distinctions | 23 Years Professional Experience")
    st.markdown("""
    **Head of Department - Computer Science & Engineering**  
    *Motivational Speaker | Coding Teacher | Chief Editor - ILDC Kids Magazine | Assistant Professor | Guest Lecturer | EMC Academic Associate | Microsoft Certified*
    """)
    st.markdown("📍 **Ayanavaram, Chennai, India** | 📧 `intellecteditor@gmail.com` | 📞 `+91 96592 09651`  \n🔗 [LinkedIn Profile](https://www.linkedin.com/in/bkalpanasattu/) | 🌐 [Official Website](https://www.bkalpana.com/about)")

with col_head2:
    # Top-right picture placeholder & interactive uploader
    st.markdown("<div style='text-align: right;'>", unsafe_allow_html=True)
    uploaded_pic = st.file_uploader("Upload Profile Photo", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
    if uploaded_pic is not None:
        st.image(uploaded_pic, caption="Dr. Kalpana B", width=150, use_container_width=False)
    else:
        # High quality default avatar svg
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", caption="Dr. Kalpana B", width=130)
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# --- QUICK METRICS DASHBOARD ROW ---
m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Total Experience", "23 Years")
m2.metric("Teaching Experience", "19.9 Years")
m3.metric("Industry Experience", "3.1 Years")
m4.metric("Academic Rank", "Rank 1 / Gold")
m5.metric("Books Authored", "2 Publications")

st.divider()

# --- TABBED & EXPANDABLE POP-OUT NAVIGATION ---
tab_summary, tab_exp, tab_edu, tab_books, tab_cert, tab_awards, tab_skills, tab_projects, tab_leadership, tab_personal = st.tabs([
    "👤 Summary",
    "💼 Experience",
    "🎓 Education",
    "📚 Books & Papers",
    "📜 Certifications",
    "🏆 Awards & Media",
    "🛠️ Tech Skills",
    "🎯 Project Domains",
    "🎤 Leadership",
    "🎨 Personal Info"
])

# --- 1. PROFESSIONAL SUMMARY ---
with tab_summary:
    st.subheader("📌 Professional Summary")
    with st.popover("🔍 Click to view Full Professional Summary", use_container_width=True):
        st.write("""
        Innovative and accomplished education professional with **23 years of experience** in engineering education, 
        academic leadership, and curriculum development. **Gold Medalist with Rank 1 distinctions** across academic milestones. 
        Proven expertise in classroom management, EdTech integration, AI/ML, Blockchain, and Python. 
        Internationally recognized as a **Microsoft Innovative Educator**, published author, motivational speaker, 
        and Doordarshan interviewee. Passionate about transforming learning through technology and student-centered pedagogy.
        """)
        st.markdown("""
        **Core Competencies:**
        - Academic Leadership & Departmental Administration (CSE, IT, CSBS, AI&DS)
        - Curriculum & Outcome-Based Education (OBE) Design
        - NAAC & NBA Accreditation Documentation
        - AI/ML, Neuro-Symbolic AI, Cloud Computing, Blockchain Research
        - Women Entrepreneurship & Career Counseling Empowerment
        """)

# --- 2. WORK EXPERIENCE ---
with tab_exp:
    st.subheader("💼 Work Experience Breakdown (23 Years Total)")
    st.info("💡 **Click any institution/role below to pop out full details & responsibilities.**")
    
    experiences = [
        {
            "role": "Head of Department – CSE",
            "institution": "JNN Institute of Engineering",
            "period": "2025 – 2026",
            "type": "Academic Leadership",
            "details": [
                "Actively managed academic and administrative responsibilities of the Computer Science and Engineering Department.",
                "Completed the Capacity Building Programme on Cybersecurity – Intermediate conducted by IIT Madras and IITM Pravartak under Malaviya Mission Teacher Training Programme, Ministry of Education (11–15 Dec 2025).",
                "Completed 5-Day International FDP on AI Innovation 2025 jointly organized by SIMATS and Strazzion LLC, North Carolina, USA (10–14 Nov 2025).",
                "Participated in 5-Day International FDP on AI-Driven Image Processing organized by Rajalakshmi Institute of Technology (8–12 Dec 2025).",
                "Featured in Daily Thanthi (15 Feb 2026) for empowering 32 women through coding, career counseling, Govt Group III & IV exam training, and social media business promotion."
            ]
        },
        {
            "role": "HOD – CSE, IT, CSBS, AI & DS",
            "institution": "Madha Engineering College",
            "period": "2024 – 2025",
            "type": "Academic Leadership",
            "details": [
                "Administered four departments simultaneously: CSE, IT, CSBS, and AI & DS.",
                "Published book 'Python Made Easy (R21 Syllabus)' by IIT Iterative International Publishers (2025).",
                "Published research paper 'A Streamlined Approach to Policy Updates in Cloud-Based Health Record Systems' in IJARIIE (Vol. 10, Issue 4, 2024).",
                "Completed NPTEL Cloud Computing course with the highest score.",
                "Completed AICTE ATAL FDP on High Performance Computing (16–21 Dec 2024)."
            ]
        },
        {
            "role": "South East Asia Head",
            "institution": "WhiteHatJr / BYJU'S",
            "period": "2020 – 2024 (3 Years, 8 Months, 27 Days)",
            "type": "Industry Leadership",
            "details": [
                "Head of South East Asia operations for online coding education platforms.",
                "Managed large-scale curriculum execution and instructor teams across international territories."
            ]
        },
        {
            "role": "Founder & CEO / Leader",
            "institution": "ILDC (Intellect Learning and Development Center) & SBAT LABS",
            "period": "2017 – 2020 (3 Years, 1 Month)",
            "type": "Entrepreneurship & Industry",
            "details": [
                "Founded ILDC Academy of Learners Chennai.",
                "Awarded Star Golden Award by NIC Academy & The Peaks Magazine in July 2022.",
                "Featured on Doordarshan Pothigai TV (6 Aug 2018) for achievement in Kids Magazine."
            ]
        },
        {
            "role": "Assistant Professor – Department of CSE",
            "institution": "Panimalar Institute of Technology (PIT)",
            "period": "2015 – 2017 (2 Years, 0 Months, 29 Days)",
            "type": "Teaching",
            "details": ["Academic teaching and engineering student mentorship."]
        },
        {
            "role": "Assistant Professor – Department of CSE",
            "institution": "Hindusthan Institute of Technology, Coimbatore",
            "period": "2010 – 2014 (4 Years, 4 Months, 28 Days)",
            "type": "Teaching & Administration",
            "details": [
                "Contributed to Examination Cell activities (exam planning, scheduling, invigilation, result processing).",
                "Developed and revised curriculum, syllabus, and Outcome-Based Education (OBE) documentation.",
                "Supported NAAC and NBA accreditation by preparing documentation and coordinating quality assurance.",
                "Prepared Course Outcomes (COs), Program Outcomes (POs), attainment analysis, and academic audit reports."
            ]
        },
        {
            "role": "Assistant Professor – Dept of CSE",
            "institution": "Alpha College of Engineering",
            "period": "2009 – 2010 (1 Year, 0 Months, 20 Days)",
            "type": "Teaching",
            "details": ["Teaching undergraduate computer science engineering courses."]
        },
        {
            "role": "Lecturer – Department of CSE",
            "institution": "WELA Malaysia",
            "period": "2007 – 2008 (0 Years, 10 Months, 22 Days)",
            "type": "International Teaching",
            "details": ["Delivered computer science curriculum in an international higher education institution in Malaysia."]
        },
        {
            "role": "Assistant Professor – Dept of CSE",
            "institution": "Sri Venkateswara College of Engineering (SVCE)",
            "period": "2004 – 2006 (2 Years, 1 Month, 4 Days)",
            "type": "Teaching",
            "details": ["Departmental academic instruction and undergraduate mentoring."]
        },
        {
            "role": "Lecturer – Dept of CSE",
            "institution": "Sri Venkateswara College of Engineering & Tech (SVCET)",
            "period": "2003 – 2004 (1 Year, 1 Month, 13 Days)",
            "type": "Teaching",
            "details": ["Lecturer in Computer Science & Engineering."]
        }
    ]

    for item in experiences:
        with st.expander(f"🔹 {item['role']} — {item['institution']} ({item['period']})"):
            st.markdown(f"**Type:** `{item['type']}`")
            for d in item['details']:
                st.markdown(f"- {d}")

# --- 3. EDUCATION ---
with tab_edu:
    st.subheader("🎓 Educational Qualifications")
    
    edu_list = [
        {
            "degree": "PhD (Pursuing) in Neuro Symbolic AI",
            "institution": "SIMATS University",
            "highlights": "Active research focus on Neuro Symbolic Artificial Intelligence."
        },
        {
            "degree": "Honorary Doctorate (2025)",
            "institution": "Europe Croatia / Oxfaa University",
            "highlights": "Awarded for outstanding contributions to education and research."
        },
        {
            "degree": "M.E. Computer Science and Engineering",
            "institution": "Anna University",
            "highlights": "First Class Distinction | CGPA: 9.0/10 | Master's Thesis: 'Shrouding in the Mobile Crowd Whereabouts and Location Confidentiality Through Collaboration'."
        },
        {
            "degree": "B.Tech Information Technology",
            "institution": "Madras University — Sri Venkateswara College of Engineering (SVCE)",
            "highlights": "First Class Distinction | 86% | Rank 1 / 67 | Major Project at Cosmosoft Technologies."
        },
        {
            "degree": "DCT (Diploma in Computer Technology)",
            "institution": "Directorate of Technical Education — Panimalar Polytechnic",
            "highlights": "Gold Medalist | 97% | Rank 1 / 65."
        }
    ]
    
    for edu in edu_list:
        with st.expander(f"🎓 {edu['degree']} — {edu['institution']}"):
            st.write(edu['highlights'])

# --- 4. BOOKS & RESEARCH PUBLICATIONS ---
with tab_books:
    st.subheader("📚 Authored Books")
    b1, b2 = st.columns(2)
    with b1:
        with st.popover("📖 Book 1: 'Mastering C and C++' (2026)", use_container_width=True):
            st.markdown("""
            - **Title:** *Mastering C and C++*
            - **Publisher:** Chyren Publications (April 2026)
            - **Availability:** Flipkart & Amazon
            - **Overview:** Comprehensive textbook guiding learners from core programming fundamentals to advanced object-oriented design in C and C++.
            """)
    with b2:
        with st.popover("📖 Book 2: 'Python Made Easy' (2025)", use_container_width=True):
            st.markdown("""
            - **Title:** *Python Made Easy (R21 Syllabus)*
            - **Publisher:** IIP Karnataka / IIT Iterative International Publishers (2025)
            - **Availability:** Flipkart & Amazon
            - **Overview:** Tailored curriculum book designed for university regulation syllabus, highlighting practical Python applications.
            """)

    st.divider()
    st.subheader("🔬 Research Publications & Presentations")
    
    pubs = [
        "**Journal Paper (2025):** 'Algorithmic Insights: Evaluating Machine Learning Techniques for Diabetic Diagnosis', *IJSRED*, Vol. 8, Issue 2 (Mar–Apr 2025).",
        "**Journal Paper (2024):** 'A Streamlined Approach to Policy Updates in Cloud-Based Health Record Systems', *IJARIIE*, Vol. 10, Issue 4 (2024).",
        "**Conference Paper (NCBAS 2014):** 'Paxos: A Larger Community Cluster to Build Consistent Data Store Using Big Data', Hindustan University (27–28 Feb 2014).",
        "**Research Paper:** 'Mobile Learning in School Perspective – The Preliminary Phase'.",
        "**Award-Winning Paper (1st Place):** 'Initial Stages of Learning Systems in Artificial Intelligence', Sathyabama Institute of Science and Technology (Feb 2002).",
        "**Award-Winning Paper (2nd Place):** 'Learning Systems in Artificial Intelligence', ISTE SVCE (Mar 2002).",
        "**Award-Winning Paper (3rd Place):** 'Genetic Algorithm', SRM Easwari Engineering College (Aug 2002).",
        "**Award-Winning Paper (4th Place):** 'GPRS and 3G WAP', SRM Easwari Engineering College (Aug 2001)."
    ]
    
    for p in pubs:
        with st.expander(p.split(':')[0].replace('*', '')):
            st.markdown(p)

# --- 5. CERTIFICATIONS ---
with tab_cert:
    st.subheader("📜 Professional Certifications & Training")
    certs = [
        "Microsoft Innovative Educator (MIE) & Minecraft Education Certified Trainer",
        "NPTEL Certification – Foundation of Cloud IoT Edge ML, IIT Kanpur (2025)",
        "NPTEL Silver Medal – Fundamentals of Algorithms and Analysis (March 2026)",
        "NPTEL Cloud Computing Certification – Highest Score Distinction",
        "Capacity Building Programme on Cybersecurity (Intermediate) – IIT Madras & IITM Pravartak (Dec 2025)",
        "AICTE ATAL FDP – High Performance Computing (16–21 Dec 2024)",
        "EMC Academic Associate – Data Science & Big Data Analytics (Dell Technologies Academic Alliance 2016)",
        "ICTACT FDP – Data Science & Big Data Analytics (2016)",
        "Python Programming Workshop – Anna University (2017)",
        "Python Certification – GUVI & IIT Madras (2017)",
        "Cisco Certified Network Associate (CCNA) (2004)"
    ]
    for c in certs:
        st.markdown(f"- 🏅 {c}")

# --- 6. AWARDS & MEDIA RECOGNITION ---
with tab_awards:
    st.subheader("🏆 Awards & Media Recognition")
    
    awards = [
        {
            "title": "Star Golden Award (July 2022)",
            "body": "Presented by NIC Academy (National Integrity Cultural Academy) & The Peaks Magazine to Mrs. B. Kalpana, Founder & CEO of Intellect Learning and Development Center (ILDC)."
        },
        {
            "title": "Doordarshan Pothigai TV Interview (August 2018)",
            "body": "Featured on 'Virundhinar Pakkam' program on 06.08.2018 recognizing achievement in Chief Editor role for ILDC Kids Magazine and educational contributions."
        },
        {
            "title": "Daily Thanthi Feature (February 2026)",
            "body": "Featured in Daily Thanthi newspaper (15 Feb 2026) for empowering 32 women through coding, career counseling, Govt Group III & IV exam training, and social media business promotion."
        },
        {
            "title": "Dina Thanthi Educational Columns (2021, 2022, 2025)",
            "body": "Featured in Ilangar Malar & Muthucharam for guiding students post-12th grade, teaching skill development through coding, and social initiatives."
        },
        {
            "title": "Academic Rank & Teaching Excellence",
            "body": "Gold Medalist in DCT (97%, Rank 1/65), Rank 1/67 in B.Tech IT (86%), and recipient of Teaching Excellence Awards across institutions."
        }
    ]
    
    for a in awards:
        with st.expander(f"⭐ {a['title']}"):
            st.write(a['body'])

# --- 7. TECHNICAL SKILLS & LANGUAGES ---
with tab_skills:
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.subheader("💻 Technical Skills")
        st.markdown("""
        - **Programming Languages:** Python, C, C++, Java, JavaScript, PHP, CGI-Perl
        - **Web & Data Technologies:** HTML, CSS, XML, SQL, Data Structures
        - **Domains:** AI/ML, Neuro-Symbolic AI, Cloud Computing, Big Data Analytics, Blockchain, IoT
        """)
    with col_s2:
        st.subheader("🗣️ Language Proficiency")
        st.progress(1.0, text="Tamil (Native / Fluent)")
        st.progress(1.0, text="English (Fluent)")
        st.progress(0.8, text="Hindi (Proficient)")
        st.progress(0.85, text="Telugu (Proficient)")
        st.progress(0.65, text="Malayalam (Working Proficiency)")

    st.divider()
    st.subheader("✍️ Editorial & Reviewer Roles")
    st.markdown("""
    - **Editor, Editorial Review Board:** *International Journal of Advanced Research in Management, Engineering and Technology (IJARMET)* (Since March 2016)
    - **Associate Editor:** *International Journal of Entrepreneurship and Small & Medium Enterprises (IJESMES)*, Kathmandu, Nepal (Since June 2015)
    - **Reviewer:** *International Journal of Advances in Engineering & Scientific Research (IJAESR)* (Since Feb 2016)
    """)

# --- 8. PROJECT GUIDANCE DOMAINS ---
with tab_projects:
    st.subheader("🎯 Project Guidance Areas")
    st.write("Dr. Kalpana B has guided student projects across 11 key engineering & tech domains:")
    
    domains = [
        "Artificial Intelligence & Machine Learning (Crop Yield, Mental Health Risk, Driver Fatigue, Voice Assistant, Vehicle Recognition)",
        "Computer Vision & Deep Learning (OCR PDF Search, Multilingual OCR, Object Tracking, Feature Fusion)",
        "Blockchain & Cyber Security (Secure Document Verification, Cloud Health Records, Dependable Computing)",
        "Data Science & Big Data Analytics (Hadoop, MapReduce, Data Virtualization, Business Analytics)",
        "Cloud Computing & Distributed Systems (Cloud Health Records, Paxos Distributed Stores)",
        "Web Technologies & Software Engineering (AI Career Portal, Food Surplus Management, Tribal E-Commerce)",
        "Computer Networks & IoT (MANET, Emergency Response Communication, GPS Tracking)",
        "Smart Transportation & Infrastructure (Road Maintenance Monitoring, Port Automation, Traffic Monitoring)",
        "Academic Administration Systems (Port Financial Automation, Reporting Workflow Automation)",
        "Educational Technology / EdTech (Mobile Learning, Online Analytics, AI Student Performance Monitoring)",
        "Healthcare Informatics (Cloud EHR, Healthcare Security, AI Mental Health Analytics)"
    ]
    for idx, d in enumerate(domains, 1):
        with st.expander(f"📌 Domain {idx}: {d.split('(')[0]}"):
            st.write(d)

# --- 9. LEADERSHIP & GUEST TALKS ---
with tab_leadership:
    st.subheader("🎤 Leadership, Chief Guest & Invited Talks")
    talks = [
        "**Chief Guest of Honour** — Natyacharyas School of Music & Dance Convocation Ceremony (10 June 2025)",
        "**Chief Guest of Honour** — Annual Day Celebration, Yogi Ram Surat Kumar Educational Academy (15 April 2025)",
        "**Chief Guest** — Orchid International School, Perumbakkam, Megathlon (15 September 2024)",
        "**Chief Guest** — Valliammal Matriculation School, Republic Day Celebration (26 January 2023)",
        "**Chief Guest & Speaker** — Jain Public School, Thirumudivakkam (2018)",
        "**Chief Guest** — 50th Annual Sports Day, Villivakkam Welfare Association (29 July 2018)",
        "**Resource Person & Speaker** — Saveetha Engineering College (19 November 2018)",
        "**Guest Lecture** — 'The New Era of Big Data' for PG students at Hindusthan Institute of Technology (28 January 2014)"
    ]
    for t in talks:
        st.markdown(f"- {t}")

# --- 10. PERSONAL INFO & HOBBIES ---
with tab_personal:
    st.subheader("🎨 Hobbies & Personal Interests")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown("""
        - 🎵 **Carnatic Vocal Singer**
        - 💃 **Bharatanatyam Dancer**
        - 🎼 **Veena Player**
        - 🍲 **Traditional Indian Cuisine**
        """)
    with col_p2:
        st.markdown("""
        - 🎨 **Fabric & Sculptural Painting**
        - 💎 **Jewellery Design**
        - 📚 **Reading Books on Child Psychology & Personality Development**
        """)
        
    st.divider()
    st.subheader("📋 Personal Details")
    st.markdown("""
    - **Date of Birth:** 04 March 1982
    - **Nationality:** Indian
    - **PAN Number:** AOXPK3503M
    - **Passport Status:** Active
    """)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>Dashboard created for Dr. Kalpana B based on authentic resume source data.</p>", unsafe_allow_html=True)
