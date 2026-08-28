from urllib.request import urlopen

# from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

MAX_DEPTH = 5
visited = set()


def crawl(url, level=0):

    if url in visited or level >= MAX_DEPTH:
        return

    print(f"🕷️ Crawling: {url} - level-{level}")
    try:
        response = urlopen(url)
    except Exception as e:
        print(f"Error occured while crawling: {e}")
        return

    # Extract html page
    html = response.read().decode("utf-8")
    # print(html)

    soup = BeautifulSoup(html, "html.parser")

    # Extract text
    text = soup.get_text(" ", strip=True)
    # print(text)
    print("   ✓ Text extracted")

    # Extract valid links
    links = []
    links_tags = soup.find_all("a")
    for link in links_tags:
        href = link.get("href")
        if href and href.startswith(("http://", "https://")):
            # print(href)
            links.append(href)

    print(f"   🔗 Found {len(links)} link(s)\n\n")

    for link in links:
        crawl(link, level + 1)


example_url = "https://example.com"

crawl(example_url)
