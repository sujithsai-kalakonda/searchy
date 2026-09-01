import string


def build_index(pages):

    index = {}

    if not pages:
        print("No pages found to index.")
        return index

    for page_id, page in pages.items():

        # First extract text
        text = page.get("text").lower()

        words = text.split()
        for word in words:

            # normalize words
            word = word.strip(string.punctuation)

            if word:
                if word not in index:
                    index[word] = set()

                # index[word].add(page.get("url"))

                index[word].add(page_id)

    return index
