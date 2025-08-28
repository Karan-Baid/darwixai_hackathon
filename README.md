# darwixai_hackathon
# Hackathon Crew Project Setup Guide

---

## 🚀 Linux-based Installation

### 1. Install uv (Astral)
```sh
wget -qO- https://astral.sh/uv/install.sh | sh
```

### 2. Install CrewAI CLI
```sh
uv tool install crewai
```

### 3. Verify Installation
```sh
uv tool list
```
You should see something like:
```sh
crewai v0.102.0

crewai
```

### 4. Create Project Directory
```sh
crewai create crew research_crew
cd research_crew
```
*Select **Groq** as the provider and **groq/gemma2-9b-it** as the model when prompted.*

### 5. Update Project Files from GitHub Repo
Update the following files:
- `src/config/agents.yaml`
- `src/config/tasks.yaml`
- `src/crew.py`
- `src/main.py`
- `src/tools/custom_tool.py`

Then run:
```sh
crewai install
```

### 6. Add API Key
Create a `.env` file in the project root and add:
```env
GROQ_API_KEY=your_api_key_here
```

### 7. Set Up Python Virtual Environment
```sh
python3 -m venv crewai_env
source crewai_env/bin/activate
pip install --upgrade pip
pip install requests beautifulsoup4 crewai

mv crewai_env .venv
source .venv/bin/activate
crewai install
```

### 8. Run the Project
```sh
crewai run
```

---

**The output will be saved in the `report.md` file in the `output` directory.**
