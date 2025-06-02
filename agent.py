from fetcher import fetch_html_text, clean_earnings_text
from summarizer import summarize_text

def run_agent(company_name="Meta", earnings_url=None):
    print(f"🔍 Starting CPO research for: {company_name}")
    if not earnings_url:
        print("❗ Please provide a specific earnings call URL.")
        return
    raw_text = fetch_html_text(earnings_url)
    cleaned = clean_earnings_text(raw_text)
    summary = summarize_text(cleaned)
    print(f"\n🧠 CPO Briefing for {company_name}:\n")
    print(summary)
