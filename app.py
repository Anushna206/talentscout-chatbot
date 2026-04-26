import streamlit as st
import re
from prompts import generate_prompt
from utils import get_llm_response


# ---------------------------
# Email Validation
# ---------------------------
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


# ---------------------------
# Page Config + Styling
# ---------------------------
st.set_page_config(page_title="TalentScout Hiring Assistant")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #f8fbff, #eef5ff);
}

h1 {
    text-align: center;
    color: #1f4e79;
    font-weight: bold;
}

.stButton>button {
    background-color: #1f77b4;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background-color: #0d5ea8;
    color: white;
}

.stTextInput input,
.stTextArea textarea {
    border-radius: 10px;
    border: 1px solid #cfd8dc;
}
</style>
""", unsafe_allow_html=True)


# ---------------------------
# Sidebar
# ---------------------------
st.title("TalentScout Hiring Assistant")

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
    width=120
)

st.sidebar.title("TalentScout")
st.sidebar.write("""
AI-Powered Recruitment Assistant

Features:
✅ Candidate Screening  
✅ Tech Assessment  
✅ Multilingual Support  
✅ Personalized Questions  
""")


# ---------------------------
# Translations
# ---------------------------
translations = {
    "English": {
        "welcome": "Hi! Welcome to TalentScout Hiring Assistant.",
        "info": "I help recruiters collect your details and assess technical skills.",
        "start": "Start Application",
        "candidate_info": "Candidate Information",
        "name": "Full Name",
        "email": "Email Address",
        "phone": "Phone Number",
        "experience": "Years of Experience",
        "position": "Desired Position",
        "location": "Current Location",
        "tech_stack": "Tech Stack",
        "submit": "Submit Details",
        "privacy": "Your data is not permanently stored.",
        "consent": "I consent to demo processing of my information",
        "chat_placeholder": "Ask for more questions or type exit",
        "thankyou": "Thank you for completing the interview process!",
        "success": "Candidate details submitted successfully!",
        "question_intro": "Thanks {name}! Based on your {experience} years of experience and interest in {position}, here are your technical questions.",
        "chat_heading": "Chat with Hiring Assistant"
    },

    "Hindi": {
        "welcome": "नमस्ते! TalentScout Hiring Assistant में आपका स्वागत है।",
        "info": "मैं आपकी जानकारी एकत्र करूँगा और तकनीकी कौशल का मूल्यांकन करूँगा।",
        "start": "आवेदन शुरू करें",
        "candidate_info": "उम्मीदवार जानकारी",
        "name": "पूरा नाम",
        "email": "ईमेल पता",
        "phone": "फोन नंबर",
        "experience": "अनुभव के वर्ष",
        "position": "वांछित पद",
        "location": "वर्तमान स्थान",
        "tech_stack": "टेक स्टैक",
        "submit": "विवरण जमा करें",
        "privacy": "आपका डेटा स्थायी रूप से संग्रहीत नहीं किया जाएगा।",
        "consent": "मैं अपनी जानकारी के डेमो उपयोग के लिए सहमति देता हूँ",
        "chat_placeholder": "और प्रश्न पूछें या exit टाइप करें",
        "thankyou": "साक्षात्कार प्रक्रिया पूरी करने के लिए धन्यवाद!",
        "success": "उम्मीदवार जानकारी सफलतापूर्वक जमा की गई!",
        "question_intro": "{name} धन्यवाद! आपके {experience} वर्षों के अनुभव और {position} में रुचि के आधार पर, ये आपके तकनीकी प्रश्न हैं।",
        "chat_heading": "Hiring Assistant से चैट करें"
    },

    "Telugu": {
        "welcome": "హాయ్! TalentScout Hiring Assistant కి స్వాగతం.",
        "info": "మీ వివరాలను సేకరించి సాంకేతిక నైపుణ్యాలను అంచనా వేస్తాను.",
        "start": "అప్లికేషన్ ప్రారంభించండి",
        "candidate_info": "అభ్యర్థి సమాచారం",
        "name": "పూర్తి పేరు",
        "email": "ఇమెయిల్ చిరునామా",
        "phone": "ఫోన్ నంబర్",
        "experience": "అనుభవ సంవత్సరాలు",
        "position": "కోరుకున్న ఉద్యోగం",
        "location": "ప్రస్తుత స్థానం",
        "tech_stack": "టెక్ స్టాక్",
        "submit": "వివరాలు సమర్పించండి",
        "privacy": "మీ డేటా శాశ్వతంగా నిల్వ చేయబడదు.",
        "consent": "నా సమాచారాన్ని డెమో ప్రయోజనాల కోసం ఉపయోగించడానికి నేను అంగీకరిస్తున్నాను",
        "chat_placeholder": "మరిన్ని ప్రశ్నలు అడగండి లేదా exit టైప్ చేయండి",
        "thankyou": "ఇంటర్వ్యూ పూర్తి చేసినందుకు ధన్యవాదాలు!",
        "success": "అభ్యర్థి వివరాలు విజయవంతంగా సమర్పించబడ్డాయి!",
        "question_intro": "{name} ధన్యవాదాలు! మీ {experience} సంవత్సరాల అనుభవం మరియు {position} పై ఆసక్తి ఆధారంగా, ఇవి మీ సాంకేతిక ప్రశ్నలు.",
        "chat_heading": "Hiring Assistant తో చాట్ చేయండి"
    }
}


# ---------------------------
# Session State
# ---------------------------
if "started" not in st.session_state:
    st.session_state.started = False

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "candidate_data" not in st.session_state:
    st.session_state.candidate_data = {}

if "language" not in st.session_state:
    st.session_state.language = "English"


# ---------------------------
# Stage 1: Greeting
# ---------------------------
if not st.session_state.started:
    st.progress(20)

    language = st.selectbox(
        "Choose Preferred Language",
        ["English", "Hindi", "Telugu"]
    )

    st.session_state.language = language
    lang = translations[language]

    st.subheader("Welcome 👋")
    st.write(lang["welcome"])
    st.write(lang["info"])

    with st.expander("How does this chatbot work?"):
        st.write("""
        1. Choose language  
        2. Enter candidate details  
        3. Get technical questions  
        4. Ask follow-up questions  
        5. Type exit anytime
        """)

    st.info(lang["privacy"])

    if st.button(lang["start"]):
        st.session_state.started = True
        st.rerun()


# ---------------------------
# Stage 2: Candidate Form
# ---------------------------
elif not st.session_state.submitted:
    st.progress(60)

    lang = translations[st.session_state.language]

    st.subheader(lang["candidate_info"])

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input(lang["name"])
        email = st.text_input(lang["email"])
        phone = st.text_input(lang["phone"])
        experience = st.text_input(lang["experience"])

    with col2:
        position = st.text_input(lang["position"])
        location = st.text_input(lang["location"])
        tech_stack = st.text_area(lang["tech_stack"])

    consent = st.checkbox(lang["consent"])

    if st.button(lang["submit"]):

        if not consent:
            st.warning("Please provide consent")

        elif not name.strip():
            st.warning("Please enter your name")

        elif not validate_email(email):
            st.warning("Please enter valid email")

        elif not phone.isdigit() or len(phone) < 10:
            st.warning("Please enter valid phone number")

        elif not experience.strip():
            st.warning("Please enter experience")

        elif not position.strip():
            st.warning("Please enter desired position")

        elif not location.strip():
            st.warning("Please enter location")

        elif not tech_stack.strip():
            st.warning("Please enter tech stack")

        else:
            st.session_state.candidate_data = {
                "name": name.strip(),
                "email": email.strip(),
                "phone": phone.strip(),
                "experience": experience.strip(),
                "position": position.strip(),
                "location": location.strip(),
                "tech_stack": tech_stack.strip()
            }

            st.session_state.submitted = True
            st.rerun()


# ---------------------------
# Stage 3: Questions + Chat
# ---------------------------
else:
    st.progress(100)

    lang = translations[st.session_state.language]
    candidate = st.session_state.candidate_data

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Experience", candidate.get("experience"))

    with col2:
        st.metric("Role", candidate.get("position"))

    with col3:
        st.metric(
            "Technologies",
            len(candidate.get("tech_stack", "").split(","))
        )

    st.success(lang["success"])

    st.write(
        lang["question_intro"].format(
            name=candidate.get("name"),
            experience=candidate.get("experience"),
            position=candidate.get("position")
        )
    )

    tech_stack = candidate.get("tech_stack")
    experience = candidate.get("experience")

    # Generate questions only once
    if len(st.session_state.chat_history) == 0:
        prompt = generate_prompt(
            tech_stack,
            experience,
            st.session_state.language
        )

        response = get_llm_response(prompt)

        st.session_state.chat_history.append({
            "role": "assistant",
            "content": response
        })

    st.subheader(lang["chat_heading"])

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_input = st.chat_input(
        lang["chat_placeholder"]
    )

    if user_input:

        if user_input.lower() in ["exit", "quit", "bye"]:
            st.success(lang["thankyou"])
            st.stop()

        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input
        })

        followup_prompt = f"""
You are TalentScout Hiring Assistant.

Respond strictly in {st.session_state.language}.

Candidate details:
Name: {candidate.get('name')}
Experience: {candidate.get('experience')}
Desired Role: {candidate.get('position')}
Tech Stack: {candidate.get('tech_stack')}

Candidate request:
{user_input}

Instructions:
- Generate more technical questions if requested
- Answer clarifications
- Stay relevant to hiring process
"""

        bot_response = get_llm_response(followup_prompt)

        st.session_state.chat_history.append({
            "role": "assistant",
            "content": bot_response
        })

        st.rerun()


# ---------------------------
# Reset Button
# ---------------------------
st.divider()

if st.button("Reset Application"):
    st.session_state.clear()
    st.rerun()