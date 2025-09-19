import requests
from bs4 import BeautifulSoup

class HiddenWikiEngine:
    def __init__(self):
        self.name = "HiddenWiki"
        self.base_url = "http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page"

    def search(self, query, limit, proxy):
        print(f"Searching {self.name} for '{query}'")
        # Contoh sederhana, karena HiddenWiki adalah direktori, bukan mesin pencari
        # Jadi kita hanya scrape halaman utama dan cari link yang mengandung query
        proxies = {
            "http": f"socks5h://{proxy}",
            "https": f"socks5h://{proxy}"
        }
        try:
            r = requests.get(self.base_url, proxies=proxies, timeout=15)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, "html.parser")
            results = []
            for link in soup.find_all("a", href=True):
                href = link['href']
                text = link.get_text()
                if query.lower() in text.lower() or query.lower() in href.lower():
                    results.append({
                        "engine": self.name,
                        "name": text.strip(),
                        "link": href.strip()
                    })
                    if limit and len(results) >= limit:
                        break
            return results
        except Exception as e:
            print(f"Error searching {self.name}: {e}")
            return []
