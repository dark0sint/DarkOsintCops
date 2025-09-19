import requests
from bs4 import BeautifulSoup

class DarkSearchEngine:
    def __init__(self):
        self.name = "DarkSearch"
        self.base_url = "http://darkfailllnkf4vf.onion/search"

    def search(self, query, limit, proxy):
        print(f"Searching {self.name} for '{query}'")
        proxies = {
            "http": f"socks5h://{proxy}",
            "https": f"socks5h://{proxy}"
        }
        params = {"q": query}
        results = []
        try:
            r = requests.get(self.base_url, params=params, proxies=proxies, timeout=15)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, "html.parser")
            for item in soup.select(".result"):
                title = item.select_one(".result-title")
                link = item.select_one("a")
                if title and link:
                    results.append({
                        "engine": self.name,
                        "name": title.get_text(strip=True),
                        "link": link['href']
                    })
                    if limit and len(results) >= limit:
                        break
            return results
        except Exception as e:
            print(f"Error searching {self.name}: {e}")
            return []
