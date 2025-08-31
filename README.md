Automated Research Assistant with DSPy and AutoGen
This project is a powerful demonstration of building robust, multi-agent AI systems using two cutting-edge frameworks: DSPy for creating reliable, self-optimizing "tools" and AutoGen for orchestrating a team of AI agents to solve complex tasks.

The system functions as an automated research assistant that can take a high-level topic, find relevant information, and synthesize it into a concise literature review.

🧠 Core Concepts & Architecture
This project moves beyond simple, brittle prompting to a more programmatic and structured approach to building with LLMs. The architecture mimics a real-world research team.

AutoGen: The AI Project Manager 🤖
AutoGen serves as the high-level orchestrator. It creates and manages a conversation between different AI agents, each with a specific role. In this project, we have:

Research Manager: The team lead that communicates with the user and directs the workflow.

Researcher: The specialist that executes tasks by using the tools provided to it.

DSPy: The Expert Tool Builder 🛠️
DSPy is used to build the specialized, high-performance "tools" that the AutoGen agents use. Instead of relying on fragile prompt engineering, DSPy allows us to define the logic of a task (its inputs and outputs). We then use a DSPy optimizer to "compile" this logic, finding the most effective and reliable prompt for the underlying LLM. This makes each tool a robust, optimized program.

System Workflow
The process flows as follows:

User Request
     │
     ▼
┌───────────────────────────┐
│ Research Manager (AutoGen)│
│  - Plans the research     │
└────────────┬──────────────┘
             │ Delegates Task
             ▼
┌───────────────────────────┐
│   Researcher (AutoGen)    │
└────────────┬──────────────┘
             │ Uses Tools
             ▼
┌───────────────────────────┐
│   DSPy-Powered Tools      │
│  - Generate Search Query  │
│  - Summarize Paper        │
│  - Synthesize Review      │
└────────────┬──────────────┘
             │ Returns Result
             ▼
┌───────────────────────────┐
│       Final Report        │
└───────────────────────────┘
✨ Key Features
Automated Research Pipeline: End-to-end workflow from topic to literature review.

Modular Agent Design: Clearly defined roles for each agent, making the system easy to extend.

Optimized AI Tools: DSPy-compiled modules ensure high-quality outputs for specialized tasks like summarization and query generation.

Programmatic Prompting: Moves beyond static f-strings to a more reliable, structured approach to interacting with LLMs.

⚙️ Tech Stack
Orchestration: Microsoft AutoGen

LLM Programming: Stanford's DSPy

Language Model: Llama 3 (via Groq API)

Core Language: Python

Utilities: python-dotenv, requests, BeautifulSoup4

📁 File Structure
dspy-autogen-researcher/
├── .env
├── main.py
├── config.py
├── agents.py
├── requirements.txt
└── tools/
    ├── __init__.py
    ├── dspy_tools.py
    └── web_tools.py
🚀 Getting Started
Follow these instructions to set up and run the project locally.

1. Prerequisites
Python 3.9+

A Groq API Key (free to create)

2. Clone the Repository
Bash

git clone https://github.com/your-username/dspy-autogen-researcher.git
cd dspy-autogen-researcher
3. Set Up a Virtual Environment
It's highly recommended to use a virtual environment.

Bash

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
4. Install Dependencies
Bash

pip install -r requirements.txt
(Note: If you don't have a requirements.txt file yet, create one with pip freeze > requirements.txt after installing the necessary packages manually.)

5. Configure Environment Variables
Rename the .env.example file (if you have one) to .env or create a new file named .env.

Add your Groq API key to the .env file:

Ini, TOML

GROQ_API_KEY="your-new-secure-groq-key"
▶️ Usage
To run the automated research assistant, execute the main script from the root directory:

Bash

python main.py
The agents will begin their conversation in the terminal, executing the research plan step-by-step.

🗺️ Future Roadmap
This project provides a solid foundation. Here are some potential improvements:

Compile DSPy Modules: Implement dspy.compile with a few-shot optimizer (BootstrapFewShot) to dramatically improve the reliability of the tools.

Add a Critic Agent: Introduce a third AutoGen agent to review and provide feedback on the generated literature review, creating an iterative improvement loop.

PDF Parsing: Add a tool using a library like PyMuPDF to allow the assistant to read and summarize academic papers from PDF files.

Integrate a Search API: Replace the basic web scraper with a robust search API like Tavily for more reliable and agent-optimized search results.
