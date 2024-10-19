import streamlit as st

# Title and Sidebar
st.title("Girls' Self-Defense Guidance")
st.sidebar.header("Navigation")
module = st.sidebar.selectbox("Choose a section", ["Self-Defense Techniques", "Safety Tips", "Emergency Contacts", "Local Resources"])

# Self-Defense Techniques with Video Tutorials
if module == "Self-Defense Techniques":
    st.header("Self-Defense Techniques")
    st.write("""
    Learn essential self-defense techniques to protect yourself in dangerous situations. 
    These techniques are simple but effective for girls of all ages.
    """)

    techniques = {
        "Blocking Attacks": "https://www.youtube.com/embed/3eLfn7Ewx_s",
        "Escaping Grabs": "https://www.youtube.com/embed/8Jx_hxyyCoE",
        "Striking Vulnerable Areas": "https://www.youtube.com/embed/Mn58owUcZgc",
        "Using Everyday Objects": "https://www.youtube.com/embed/hcJrS3r24B0"
    }

    technique_choice = st.selectbox("Choose a technique to learn", list(techniques.keys()))
    st.video(techniques[technique_choice])

# Safety Tips Section
elif module == "Safety Tips":
    st.header("Safety Tips")
    st.write("""
    Here are some essential safety tips for girls to help prevent dangerous situations:
    """)
    
    tips = [
        "Always be aware of your surroundings, especially in unfamiliar areas.",
        "Avoid walking alone at night; if necessary, stay in well-lit areas.",
        "Keep your phone fully charged and easily accessible in case of emergency.",
        "Trust your instincts. If you feel uncomfortable or unsafe, leave the situation immediately.",
        "Let someone know where you are and where you are going, especially when going out alone."
    ]

    for i, tip in enumerate(tips, 1):
        st.write(f"**{i}. {tip}**")

    if st.button("More Safety Tips"):
        st.write("""
        - Avoid distractions like texting or listening to music loudly while walking.
        - Carry a small, personal safety tool (such as a whistle or pepper spray) for emergencies.
        - Stay away from isolated areas and always try to walk in groups.
        - Take self-defense classes to learn how to protect yourself in risky situations.
        - In a dangerous situation, yell for help to attract attention.
        """)

# Emergency Contacts Section
elif module == "Emergency Contacts":
    st.header("Emergency Contacts")
    st.write("""
    Keep these emergency contacts in mind for quick access when needed.
    """)

    st.write("### Emergency Numbers")
    st.write("**Police Emergency Number**: 911")
    st.write("**Local Women’s Helpline**: 800-799-SAFE (7233)")
    st.write("**Local Hospital**: 555-123-4567")
    st.write("**Fire Department**: 555-987-6543")
    
    st.write("### How to Call for Help")
    st.write("""
    - Stay calm and provide clear details about your location and the nature of the emergency.
    - If you're unable to speak, try to send a text message or use emergency alert apps.
    """)

# Local Resources and Helplines Section
elif module == "Local Resources":
    st.header("Local Resources and Helplines")
    st.write("""
    Find support from local organizations and helplines that provide assistance for women in need.
    """)

    resources = {
        "Women's Shelter": "Provides shelter and support for women in crisis. Call 555-876-5432.",
        "Legal Aid": "Get free legal advice and representation for women's safety. Call 555-345-6789.",
        "Counseling Services": "Offers confidential counseling for women. Call 555-432-1234.",
        "Self-Defense Classes": "Join free self-defense classes for women. Visit www.defenseclasses.org"
    }

    for resource, description in resources.items():
        st.write(f"**{resource}:** {description}")

    st.write("""
    For more information, visit local women's centers or call the helplines listed above.
    """)

# Deploy the app using: streamlit run app.py
