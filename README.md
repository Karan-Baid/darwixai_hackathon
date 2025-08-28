
# Research Crew

Welcome to **Research Crew** – a modular, extensible research automation framework powered by [crewAI](https://crewai.com). This project helps you set up a multi-agent AI system with ease, enabling agents to collaborate on complex tasks and maximize their collective intelligence.


---

## 🚀 Getting Started
# darwixai_hackathon
# Hackathon Crew Project Setup Guide

**Linux based installation**

1. Install uv (Astral):
   
	wget -qO- https://astral.sh/uv/install.sh | sh

2. Install CrewAI CLI:

	uv tool install crewai

3. Verify installation:
   
	uv tool list


You should see something like:

	crewai v0.102.0

	crewai

4. Create project directory:

	crewai create crew research_crew
    
	cd research_crew

**(Select Groq as the provider and select groq/gemma2-9b-it)**

5. Update project files from the GitHub repo:
   
   - src/config/agents.yaml
   - src/config/tasks.yaml
   - src/crew.py
   - src/main.py
   - src/tools/custom_tool.py
     
   Run the command:

	  crewai install

6. Add API key:
   Create a .env file in the project root and add:

   GROQ_API_KEY=your_api_key_here

7. Run the following commands :

	python3 -m venv crewai_env
    
	source crewai_env/bin/activate

	pip install --upgrade pip

	pip install requests beautifulsoup4 crewai

	deactivate

	mv crewai_env .venv

	source .venv/bin/activate

	crewai install

8. Run the project:
    
	  crewai run

**The output will be saved in the report.md file in the output directory.**

