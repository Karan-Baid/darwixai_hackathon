# darwixai_hackathon
# Hackathon Crew Project Setup Guide

1. Install uv (Astral):
wget -qO- https://astral.sh/uv/install.sh | sh

2. Install CrewAI CLI:
uv tool install crewai

3. Verify installation:
uv tool list
You should see something like:
crewai v0.102.0
* crewai

4. Create project directory:
crewai create crew research_crew
cd research_crew
(Select Groq as the provider and any model you like)

5. Update project files from the GitHub repo:
- src/config/agents.yaml
- src/config/tasks.yaml
- src/crew.py
- src/main.py
- src/tools/custom_tool.py


7. Add API key:
Create a .env file in the project root and add:
GROQ_API_KEY=your_api_key_here

8. Run the project:
crewai run
