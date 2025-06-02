import time

def search_all_sources(company_name):
    def safe_search(term):
        try:
            return search_links(company_name, term)
        except Exception as e:
            print(f"⚠️ Error while searching '{term}':", e)
            return []
    
    return {
        "10k": safe_search("10-K site:sec.gov"),
        "earnings_call": safe_search("earnings call transcript site:fool.com"),
        "interview": safe_search("CEO interview site:youtube.com"),
        "newsroom": safe_search(f"press room site:{company_name.lower()}.com"),
        "linkedin": safe_search("linkedin CEO post"),
    }
def search_links(company_name, query_suffix, num_results=5):
    query = f"{company_name} {query_suffix}"
    with DDGS() as ddgs:
        time.sleep(5)  # Add delay to avoid rate limit
        results = [r for r in ddgs.text(query, max_results=num_results)]
    return [r['href'] for r in results]
