def fetch_html_text(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"❌ Error {response.status_code} for URL: {url}")
            return ""
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove script/style
        for tag in soup(["script", "style", "noscript"]):
            tag.extract()

        text = soup.get_text(separator="\n")
        lines = [line.strip() for line in text.splitlines()]
        text = "\n".join([line for line in lines if line])
        return text
    except Exception as e:
        print(f"❌ Failed to parse HTML: {e}")
        return ""
