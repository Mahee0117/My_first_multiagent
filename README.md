# 🤖 Multi-Agent AI Content Studio

AI-powered content generation using **CrewAI + Hugging Face + Qwen + Streamlit**.

## 🚀 Workflow

```text
User Topic
    ↓
🧠 Planner Agent
    ↓
✍️ Writer Agent
    ↓
📝 Editor Agent
    ↓
✨ Final Article
🧠 Agents
Agent	Responsibility
🧠 Planner	Creates the content plan, structure and keywords
✍️ Writer	Generates the article from the plan
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

export HF_TOKEN="your_huggingface_token"

Run the application:

python -m streamlit run project1.py
📂 Project Structure
crewai-project/
├── project1.py
├── requirements.txt
├── README.md
└── assets/
🎯 Example

Input:

Artificial Intelligence

Process:

Artificial Intelligence
        ↓
      Planner
        ↓
   Content Plan
        ↓
      Writer
        ↓
    Draft Article
        ↓
      Editor
        ↓
   Final Article
✨ Features
🤖 Multi-agent AI workflow
🔄 Sequential agent execution
🧠 Specialized agent roles
🤗 Hugging Face LLM integration
🎨 Streamlit web interface
📄 Markdown article generation
📚 Key Concepts
Multi-Agent Systems
CrewAI
Agent & Task Design
Sequential Workflows
LLM Integration
Prompt Engineering
Streamlit
👨‍💻 Author

Mahesh M S K

Computer Science Student |
