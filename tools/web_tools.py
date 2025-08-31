import requests
from bs4 import BeautifulSoup


def search_and_scrape(query: str) -> str:
    """Searches a query and scrapes the text from the first result."""
    print(f"\n>>>> Executing Web Search: {query}")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        search_url =  f"https://html.duckduckgo.com/html/?q={query}"
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        first_link = soup.find('a', class_='result__a')
        
        if not first_link or not first_link.has_attr('href'):
            return "Could not find a valid search result link."
            
        paper_url = first_link['href']
        print(f">>>> Scraping URL: {paper_url}")
        
        paper_response = requests.get(paper_url, headers=headers)
        paper_response.raise_for_status()
        paper_soup = BeautifulSoup(paper_response.text, 'html.parser')
        
        paragraphs = paper_soup.find_all('p')
        content = "\n".join([p.get_text() for p in paragraphs])
        
        if not content:
            return "Could not extract text content from the page."
            
        return content[:8000] # Truncate for efficiency
    except requests.RequestException as e:
        return f"An error occurred during the web request: {e}"
    