import os
from summarizer import summarize_text


def load_text(file_path):
    """Return file content if it exists, else empty string."""
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""


def summarize_section(header, text):
    """Return formatted summary for a text section."""
    if not text:
        return ""
    summary = summarize_text(text)
    return f"## {header}\n{summary}\n"


def run_cpo_research(company_name, base_dir="data"):
    """Compile a CPO research brief for the given company.

    This function looks for text files under `base_dir/company_name/`.
    The following filenames are recognized:
        - mission.txt
        - vision.txt
        - strategy.txt
        - revenue_drivers.txt
        - competitors.txt
        - differentiation.txt
        - market_share.txt
        - case_studies.txt
        - strategic_bets.txt
        - investor_calls.txt
        - leadership_interviews.txt
        - acquisitions.txt
        - partnerships.txt
        - linkedin_posts.txt
        - earnings_calls.txt
        - press_briefings.txt
    """
    company_dir = os.path.join(base_dir, company_name.lower())
    sections = {
        "Mission": "mission.txt",
        "Vision": "vision.txt",
        "Strategy": "strategy.txt",
        "Revenue Drivers": "revenue_drivers.txt",
        "Competitors": "competitors.txt",
        "Differentiation & Moat": "differentiation.txt",
        "Market Share": "market_share.txt",
        "Case Studies": "case_studies.txt",
        "Strategic Bets": "strategic_bets.txt",
        "Investor Calls & 10-K Filings": "investor_calls.txt",
        "Leadership Interviews": "leadership_interviews.txt",
        "Acquisitions": "acquisitions.txt",
        "Partnerships": "partnerships.txt",
        "LinkedIn Posts": "linkedin_posts.txt",
        "Earnings Calls": "earnings_calls.txt",
        "Press Briefings": "press_briefings.txt",
    }

    report_sections = []
    for header, filename in sections.items():
        text = load_text(os.path.join(company_dir, filename))
        summary = summarize_section(header, text)
        if summary:
            report_sections.append(summary)

    final_report = "\n".join(report_sections)
    if not final_report:
        final_report = f"No data available for {company_name}."
    return final_report


if __name__ == "__main__":
    name = input("Enter company name: ")
    print(run_cpo_research(name))
