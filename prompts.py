# Generates prompt for initial technical assessment
# Questions are personalized based on:
# - Tech stack
# - Experience level
# - Selected language
def generate_prompt(tech_stack, experience, language):
    return f"""
You are TalentScout's AI Hiring Assistant.

Respond strictly in {language} language.

Candidate has:
{experience} years of experience

Tech Stack:
{tech_stack}

Instructions:
1. Generate 5 technical interview questions
2. Cover each technology mentioned
3. Match difficulty based on experience:
   - 0-2 years → beginner/intermediate
   - 3+ years → intermediate/advanced
4. Keep questions concise
5. Return only numbered questions
6. Questions must be in {language}
"""