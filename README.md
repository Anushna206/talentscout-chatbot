
# TalentScout Hiring Assistant Chatbot

## Project Overview

TalentScout Hiring Assistant is an AI-powered recruitment chatbot developed to automate the initial screening process for technical candidates.

The chatbot helps recruiters by:

- Greeting candidates
- Collecting essential candidate details
- Understanding candidate tech stack
- Generating personalized technical interview questions
- Supporting follow-up conversations
- Maintaining context-aware interactions
- Providing multilingual support
- Ensuring privacy awareness during data collection


---

# Capabilities

### Candidate Information Collection
The chatbot collects:

- Full Name  
- Email Address  
- Phone Number  
- Years of Experience  
- Desired Position  
- Current Location  
- Tech Stack  

---

### Technical Question Generation
Based on the candidate’s declared tech stack, the chatbot generates relevant interview questions.

Example:

If a candidate enters:

- Python  
- SQL  
- AWS  

The chatbot generates role-specific technical questions for these technologies.

---

### Follow-up Interaction
Candidates can continue interacting with the chatbot by:

- Asking for more questions  
- Requesting easier/harder questions  
- Asking clarifications  
- Ending the conversation anytime  

---

### Multilingual Support
The chatbot supports:

- English  
- Hindi  
- Telugu  

The entire interface and chatbot responses adapt based on the selected language.

---

### Personalized Responses
Questions are tailored based on:

- Candidate experience level  
- Desired role  
- Tech stack  

---

### UI Enhancements
- Progress indicators  
- FAQ section  
- Sidebar branding  
- Metrics dashboard  
- Custom styling  

---

# Installation Instructions

## Step 1: Clone Repository

```bash
git clone <your_github-repository-link>
```

---

## Step 2: Navigate to Project Folder

```bash
cd talentscout-chatbot
```

---

## Step 3: Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 4: Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 6: Configure API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## Step 7: Run Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# Usage Guide

### Step 1: Launch Application
Run the Streamlit application locally.

---

### Step 2: Select Preferred Language
Choose:

- English  
- Hindi  
- Telugu  

---

### Step 3: Read Chatbot Introduction
The chatbot explains its purpose and privacy notice.

---

### Step 4: Enter Candidate Details
Provide:

- Name  
- Email  
- Phone Number  
- Experience  
- Desired Position  
- Location  
- Tech Stack  

---

### Step 5: Provide Consent
The user must agree to demo data processing.

---

### Step 6: Receive Technical Questions
The chatbot generates technical questions based on:

- Tech stack  
- Experience level  

---

### Step 7: Continue Chatting
Candidates can request:

- More questions  
- Clarifications  
- Additional assistance  

---

### Step 8: End Conversation
Type:

```text
exit
```

to end the interview.

---

# Technical Details

## Frontend
:contentReference[oaicite:0]{index=0}

Used to build the chatbot user interface.

---

## Programming Language
:contentReference[oaicite:1]{index=1}

Used for backend logic and application development.

---

## LLM Provider
:contentReference[oaicite:2]{index=2}

Used for generating technical interview questions and follow-up responses.

---

## Model Used

```text
llama-3.3-70b-versatile
```

---

## Environment Management
:contentReference[oaicite:3]{index=3}

Used to securely load API keys.

---

# Architectural Decisions

```text
User Interface (Streamlit)
        ↓
Session State Management
        ↓
Candidate Information Collection
        ↓
Prompt Generation
        ↓
Groq LLM API
        ↓
Technical Question Generation
        ↓
Follow-up Interaction
```

### Why Streamlit?
- Fast development
- Easy deployment
- Interactive UI components

### Why Groq?
- Fast inference
- Free API access
- Easy Llama model integration

### Why Session State?
Streamlit reruns scripts after every interaction.  
`st.session_state` was used to maintain conversation flow.

---

# Prompt Design

Two prompts were designed:

---

## 1. Candidate Technical Question Prompt

This prompt uses:

- Candidate tech stack  
- Years of experience  
- Preferred language  

Prompt goals:

- Generate relevant questions  
- Cover all mentioned technologies  
- Adjust difficulty based on experience  
- Return concise interview questions  

Example:

```text
Generate technical questions for Python, SQL, AWS candidate with 3 years experience
```

---

## 2. Follow-up Conversation Prompt

This prompt handles:

- Additional question requests  
- Clarifications  
- Difficulty changes  
- Context-aware responses  

It ensures the chatbot remains relevant to the hiring process.

---

# Challenges Faced & Solutions

---

## Challenge 1: API Authentication Issues

### Problem:
Groq API authentication failed.

### Solution:
Fixed `.env` configuration and regenerated API keys.

---

## Challenge 2: Deprecated Model

### Problem:
Older model:

```text
llama3-8b-8192
```

was deprecated.

### Solution:
Migrated to:

```text
llama-3.3-70b-versatile
```

---

## Challenge 3: Streamlit Rerun Problem

### Problem:
Application state was resetting after every interaction.

### Solution:
Implemented `st.session_state` for maintaining conversation flow.

---

## Challenge 4: Multilingual Support

### Problem:
Only technical questions were changing language.

### Solution:
Implemented translation dictionaries for full UI localization.

---

## Challenge 5: Better User Experience

### Problem:
Default Streamlit UI looked basic.

### Solution:
Added styling, progress bars, metrics, and FAQ sections.

---

# Data Privacy

- User consent is required  
- No permanent storage of personal information  
- Uses simulated/demo candidate data  
- Avoids unnecessary sensitive data retention  

---

# Future Improvements

- Resume parsing  
- Sentiment analysis  
- Candidate scoring system  
- Recruiter dashboard  
- Database integration  

---


# GitHub Repository

https://github.com/Anushna206/talentscout-chatbot
