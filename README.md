# Company Research Agent 🧠

This is a free, end-to-end AI agent that creates CPO-ready executive briefings from a company’s earnings call.

### 🔍 What it does
- Fetches transcript from an earnings call link
- Cleans out non-essential sections
- Summarizes the key strategic highlights using an LLM
- Outputs an executive research brief

### ✅ How to Use (in Colab)
1. Clone this repo into Colab or local Jupyter
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
### ✅ Import & run
from agent import run_agent
run_agent("Meta", earnings_url="https://...")
