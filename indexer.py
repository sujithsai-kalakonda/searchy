import string
import math


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


def calculate_idf(word, total_pages, index):
    """
    N = Total pages
    DF = No of pages in which the word occurs
    IDF = log(N / DF)
    """

    DF = len(index.get(word, {}))

    IDF = math.log10(total_pages / DF)
    # print(f"The IDF for word '{word}' is {IDF}\n")

    return IDF


def calculate_tf_idf(word, page_id, index, total_pages):
    """
    - Get words dictionary from index
    - Calculate the frequency for page_id
    - Calculate TF
    - Calculate IDF
    - return TF x IDF
    """

    word_page_dict = index.get(word)

    TF = word_page_dict.get(page_id)

    IDF = calculate_idf(word, total_pages, index)
    TF_IDF = TF * IDF
    # print(f"TF-IDF for word '{word}' is {TF_IDF}")

    return TF_IDF
