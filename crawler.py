from urllib.request import urlopen

# from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

MAX_DEPTH = 2
visited = set()


def crawl(url, pages, level=0, page_id=1):

    if url in visited or level >= MAX_DEPTH:
        return

    print(f"🕷️ Crawling: {url} - level-{level}")
    try:
        response = urlopen(url)
    except Exception as e:
        print(f"Error occured while crawling: {e}")
        return

    # Extract html page
    try:
        html = response.read().decode("utf-8")
        # print(html)
    except Exception as e:
        print(f"Error reading: {e}\n")
        return

    soup = BeautifulSoup(html, "html.parser")

    # Get the title text
    web_title = soup.title.string

    # Extract text
    text = soup.get_text(" ", strip=True)
    # print(text)
    print("   ✓ Text extracted")

    pages[page_id] = {"url": url, "title": web_title, "text": text}

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
        page_id += 1
        crawl(link, pages, level + 1, page_id)


if __name__ == "__main__":
    example_url = "https://example.com"

    # pages = []
    pages = {}
    crawl(example_url, pages=pages)

    # print("\n\n")
    # print(pages)
    # print("\n\n")

    from indexer import build_index

    print("**INDEX**")
    print(build_index(pages))
