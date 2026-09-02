from crawler import crawl
from indexer import build_index
from searcher import search


def main():

    pages = {}

    # Example URL
    example_url = "https://example.com"

    # Crawl
    crawl(example_url, pages=pages)

    # with open("sample_pages.txt", "w", encoding="utf-8") as f:
    #     f.write(str(pages))

    # Build Index
    index = build_index(pages)

    print(f"INDEX: {index}\n\n")

    print("========================")
    print("       SEARCHY 🔎       ")
    print("========================")

    while True:
        query = input("Type your query: ")
        if query.lower().strip() == "exit":
            print("GoodBye 👋....")
            return

        print("searching.....")

        res = search(query, index, len(pages))
        if res:
            for idx, key in enumerate(res):
                print()

                org_key = pages.get(key, {})  # Fetch page metada using page_id

                print(f"{idx+1}. {org_key.get("title", "")}")
                print()
                print(f"   {org_key.get("url", None)}")
                print()
                print(f"   score: {res[key]}")
        else:
            print("OOPS! No result found....")
            print()


if __name__ == "__main__":
    main()
