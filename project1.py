import os
import streamlit as st

st.set_page_config(page_title="Content Studio", layout="centered")
st.title("Content Studio")
st.caption("AI-assisted planning, writing, and editing")

with st.form("article_form"):
    topic = st.text_input("Article topic", value="Artificial Intelligence")
    submitted = st.form_submit_button("Generate article", type="primary")

if not submitted:
    st.stop()
from crewai import Agent, Task, Crew, LLM


# ============================================================
# 1. HUGGING FACE LLM
# ============================================================

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    st.error("HF_TOKEN is not set. Add your Hugging Face token to the environment, then restart the app.")
    st.stop()

llm = LLM(
    model="huggingface/Qwen/Qwen3-4B-Instruct-2507",
    api_key=HF_TOKEN
)

print("Hugging Face LLM configured successfully!")


# ============================================================
# 2. PLANNER AGENT
# ============================================================

planner = Agent(
    role="Content Planner",
    goal="Plan engaging and factually accurate content on {topic}",
    backstory=(
        "You're working on planning a blog article "
        "about the topic: {topic}. "
        "You collect information that helps the audience "
        "learn something and make informed decisions. "
        "Your work is the basis for the Content Writer "
        "to write an article on this topic."
    ),
    allow_delegation=False,
    verbose=False,
    llm=llm
)

print("Planner agent created successfully!")


# ============================================================
# 3. WRITER AGENT
# ============================================================

writer = Agent(
    role="Content Writer",
    goal=(
        "Write insightful and factually accurate "
        "opinion piece about the topic: {topic}"
    ),
    backstory=(
        "You're working on writing a new opinion piece "
        "about the topic: {topic}. "
        "You base your writing on the work of the "
        "Content Planner, who provides an outline "
        "and relevant context about the topic. "
        "You follow the main objectives and direction "
        "of the outline as provided by the Content Planner. "
        "You also provide objective and impartial insights "
        "and back them up with information provided "
        "by the Content Planner. "
        "You acknowledge in your opinion piece "
        "when your statements are opinions "
        "as opposed to objective statements."
    ),
    allow_delegation=False,
    verbose=False,
    llm=llm
)

print("Writer agent created successfully!")


# ============================================================
# 4. EDITOR AGENT
# ============================================================

editor = Agent(
    role="Editor",
    goal=(
        "Edit a given blog post to align with "
        "the writing style of the organization."
    ),
    backstory=(
        "You are an editor who receives a blog post "
        "from the Content Writer. "
        "Your goal is to review the blog post "
        "to ensure that it follows journalistic best practices, "
        "provides balanced viewpoints when providing "
        "opinions or assertions, "
        "and also avoids major controversial topics "
        "or opinions when possible."
    ),
    allow_delegation=False,
    verbose=False,
    llm=llm
)

print("Editor agent created successfully!")


# ============================================================
# 5. PLAN TASK
# ============================================================

plan = Task(
    description=(
        "1. Prioritize the latest trends, key players, "
        "and noteworthy news on {topic}.\n"
        "2. Identify the target audience, considering "
        "their interests and pain points.\n"
        "3. Develop a detailed content outline including "
        "an introduction, key points, and a call to action.\n"
        "4. Include SEO keywords and relevant data or sources."
    ),
    expected_output=(
        "A comprehensive content plan document "
        "with an outline, audience analysis, "
        "SEO keywords, and resources."
    ),
    agent=planner
)


# ============================================================
# 6. WRITE TASK
# ============================================================

write = Task(
    description=(
        "1. Use the content plan to craft a compelling "
        "blog post on {topic}.\n"
        "2. Incorporate SEO keywords naturally.\n"
        "3. Sections/Subtitles are properly named "
        "in an engaging manner.\n"
        "4. Ensure the post is structured with an "
        "engaging introduction, insightful body, "
        "and a summarizing conclusion.\n"
        "5. Proofread for grammatical errors and "
        "alignment with the brand's voice.\n"
    ),
    expected_output=(
        "A well-written blog post "
        "in markdown format, ready for publication, "
        "each section should have 2 or 3 paragraphs."
    ),
    agent=writer
)


# ============================================================
# 7. EDIT TASK
# ============================================================

edit = Task(
    description=(
        "Proofread the given blog post for "
        "grammatical errors and "
        "alignment with the brand's voice."
    ),
    expected_output=(
        "A well-written blog post in markdown format, "
        "ready for publication, "
        "each section should have 2 or 3 paragraphs."
    ),
    agent=editor
)


# ============================================================
# 8. CREATE CREW
# ============================================================

crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=False
)

print("Crew created successfully!")


# ============================================================
# 9. RUN CREW
# ============================================================

result = crew.kickoff(
    inputs={
        "topic": topic.strip()
    }
)


# ============================================================
# 10. DISPLAY RESULT
# ============================================================

st.markdown(str(result))
st.download_button(
    "Download article",
    data=str(result),
    file_name="article.md",
    mime="text/markdown",
)