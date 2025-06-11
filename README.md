# Company Research Agent 🧠

This project provides lightweight tools for generating CPO-ready briefs from company materials.

## 🔍 Features
- Summarize earnings call transcripts from a given URL
- Generate a multi-section research report from local text files

## 📦 Installation
1. Clone this repo into Colab or a local environment
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ✅ Usage
### Earnings Call Summaries
```python
from agent import run_agent
run_agent("Meta", earnings_url="https://...")
```

### Comprehensive CPO Research
Prepare a directory `data/<company_name>/` with text files such as `mission.txt`, `strategy.txt`, `investor_calls.txt`, etc. Then run:
```python
from cpo_research_agent import run_cpo_research
print(run_cpo_research("acme"))
```
This will produce a brief with section headers for each available file.
