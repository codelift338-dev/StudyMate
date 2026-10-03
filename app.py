import os
from openai import OpenAI
import streamlit as st


# ============================================================
# Page configuration
# ============================================================

st.set_page_config(
    page_title="StudyMate",
    page_icon="📚",
    layout="centered"
)


# ============================================================
# AI configuration
# ============================================================

token = os.environ.get("HF_TOKEN")

if not token:
    st.error("Hugging Face token is not available.")
    st.stop()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=token,
)

MODEL = "google/gemma-3-4b-it"


# ============================================================
# Helper function
# ============================================================

def ask_ai(instruction, notes, subject, difficulty):

    prompt = f"""
You are StudyMate, an AI study assistant designed for
Computer Science and Engineering students.

Subject:
{subject}

Difficulty level:
{difficulty}

Study notes:
--- START NOTES ---
{notes}
--- END NOTES ---

Task:
{instruction}

Important rules:
- Use only information supported by the notes whenever possible.
- Do not invent facts.
- Explain technical terms clearly.
- Use simple language while keeping technical accuracy.
- Focus on exam preparation.
- Use headings, bullet points, tables, or numbered lists when useful.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=800,
    )

    return response.choices[0].message.content


# ============================================================
# Header
# ============================================================

st.title("📚 StudyMate")

st.subheader("Your AI-powered exam companion")

st.write(
    "Built for a college student who wants to turn long "
    "engineering notes into quick, understandable study material."
)

st.divider()


# ============================================================
# Study settings
# ============================================================

col1, col2 = st.columns(2)

with col1:
    subject = st.selectbox(
        "📘 Subject",
        [
            "Data Structures & Algorithms",
            "Database Management Systems",
            "Operating Systems",
            "Computer Networks",
            "Object-Oriented Programming",
            "Software Engineering",
            "Computer Architecture",
            "Other"
        ]
    )

with col2:
    difficulty = st.selectbox(
        "🎯 Level",
        [
            "Beginner",
            "Intermediate",
            "Exam Preparation"
        ]
    )


# ============================================================
# Notes
# ============================================================

notes = st.text_area(
    "📖 Paste your study notes",
    height=300,
    placeholder=(
        "Paste your long lecture notes here...\n\n"
        "Example:\n"
        "Normalization is a database design technique..."
    )
)


# ============================================================
# Actions
# ============================================================

st.write("### What do you want to do?")

col1, col2 = st.columns(2)

with col1:

    summarize = st.button(
        "📝 Summarize",
        use_container_width=True
    )

    explain = st.button(
        "💡 Explain",
        use_container_width=True
    )

with col2:

    quiz = st.button(
        "❓ Quiz Me",
        use_container_width=True
    )

    flashcards = st.button(
        "🃏 Flashcards",
        use_container_width=True
    )


# ============================================================
# AI actions
# ============================================================

if summarize:

    if not notes.strip():

        st.warning("Please paste your notes first.")

    else:

        with st.spinner("Creating your exam summary..."):

            answer = ask_ai(
                """
Create concise exam revision notes.

Include:
1. Important concepts
2. Key definitions
3. Important facts
4. Important technical terms
5. A short "Remember This" section

Remove unnecessary repetition.
""",
                notes,
                subject,
                difficulty
            )

        st.subheader("📝 Exam Summary")
        st.markdown(answer)


if explain:

    if not notes.strip():

        st.warning("Please paste your notes first.")

    else:

        with st.spinner("Explaining the concepts..."):

            answer = ask_ai(
                """
Explain the most important concepts from these notes.

For difficult technical concepts:
- Explain them step by step.
- Give a simple real-world analogy when useful.
- Give a small technical example when appropriate.
- Point out common exam mistakes.
""",
                notes,
                subject,
                difficulty
            )

        st.subheader("💡 Simple Explanation")
        st.markdown(answer)


if quiz:

    if not notes.strip():

        st.warning("Please paste your notes first.")

    else:

        with st.spinner("Creating your practice quiz..."):

            answer = ask_ai(
                """
Create an exam practice quiz.

Create:
- 5 multiple-choice questions.
- 3 conceptual questions.
- 2 challenging questions.

For multiple-choice questions:
- Give four options.
- Clearly identify the correct answer.
- Briefly explain why it is correct.

Put the answer key after all questions.
""",
                notes,
                subject,
                difficulty
            )

        st.subheader("❓ Practice Quiz")
        st.markdown(answer)


if flashcards:

    if not notes.strip():

        st.warning("Please paste your notes first.")

    else:

        with st.spinner("Creating your flashcards..."):

            answer = ask_ai(
                """
Create 10 exam-focused flashcards.

For every flashcard use:

### Question
[question]

### Answer
[short answer]

Focus on:
- Definitions
- Important concepts
- Differences between concepts
- Technical terminology
- Common exam questions
""",
                notes,
                subject,
                difficulty
            )

        st.subheader("🃏 Flashcards")
        st.markdown(answer)


# ============================================================
# Footer
# ============================================================

st.divider()

st.caption(
    "🤖 Powered by an open-weight AI model through Hugging Face."
)

st.caption(
    "StudyMate was built to help a real college friend "
    "study more effectively from long technical notes."
)
