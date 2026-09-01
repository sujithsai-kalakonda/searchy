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
                    # index[word] = set() # this tells whether a word occured in a page/url

                    index[word] = {
                        page_id: 1
                    }  # Now alon with the page_ids we also store the freq of the word occuring in that page_id i.e TF - Term Frequency

                elif page_id in index[word]:
                    index[word][page_id] += 1

                else:
                    index[word][page_id] = 1

                # index[word].add(page_id)

    return index
