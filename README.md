# 🤖 Multi-Agent AI Content Studio

> AI-powered content generation using **CrewAI + Hugging Face + Qwen + Streamlit**

## 🚀 Overview

A multi-agent AI application that converts a topic into a refined article using three specialized agents:

```text
User Topic
    ↓
🧠 Planner
    ↓
✍️ Writer
    ↓
📝 Editor
    ↓
✨ Final Article
🧠 Agents
Agent	Role
🧠 Planner	Creates content plan, structure and keywords
✍️ Writer	Generates the article
📝 Editor	Reviews and refines the article
🛠️ Tech Stack
Python 3.11
CrewAI
Hugging Face
Qwen3-4B-Instruct
LiteLLM
Streamlit
⚙️ Setup
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

python3.11 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

Set your Hugging Face token:

export HF_TOKEN="your_token"

Run:

python -m streamlit run project1.py
📂 Project Structure
crewai-project/
├── project1.py
├── requirements.txt
├── README.md
└── assets/
🎯 Example

Input

Artificial Intelligence

Output

A structured and edited Markdown article generated through the Planner → Writer → Editor workflow.

🔄 Architecture
             Streamlit
                 │
                 ▼
             CrewAI
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
     Planner → Writer → Editor
                 │
                 ▼
           Final Article
📚 Learning

This project demonstrates:

Multi-Agent AI
CrewAI orchestration
Agent & Task design
Sequential workflows
Hugging Face LLM integration
Streamlit AI applications
👨‍💻 Author

Mahesh M S K

Computer Science Student | AI & DevOps Enthusiast
