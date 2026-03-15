import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import sys

start_url = sys.argv[1]
visited = set()
all_links = set()
MAX_PAGES = 40
BLOCKED_EXTENSIONS = (
    ".jpg", ".jpeg", ".png", ".gif", ".svg",
    ".css", ".js", ".mp4", ".mp3", ".zip"
)

def get_links(url):
    try:
        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        )
        soup = BeautifulSoup(response.text, "html.parser")
        links = []
        for tag in soup.find_all("a", href=True):
            link = urljoin(url, tag["href"])
            if link.startswith("http"):
                links.append(link)
        return links
    except Exception as e:
        print("Error reading:", url, e)
        return []

def crawl(url):
    if url in visited:
        return
    if len(visited) >= MAX_PAGES:
        return
    if url.lower().endswith(BLOCKED_EXTENSIONS):
        return
    print("Crawling:", url)
    visited.add(url)
    links = get_links(url)
    for link in links:
        if link.lower().endswith(BLOCKED_EXTENSIONS):
            continue
        if link not in all_links:
            all_links.add(link)
        if link not in visited:
            crawl(link)


crawl(start_url)
print("\nTotal links collected:", len(all_links))

with open("urls.txt", "w", encoding="utf-8") as f:
    for link in sorted(all_links):
        f.write(link + "\n")

print("Saved to urls.txt")