import string
from operator import itemgetter
from indexer import calculate_idf, calculate_tf_idf


def search(query: str, index: dict, total_pages: int):
    # split and normalize the query
    query_words = []

    for word in query.split():
        word = word.lower()
        word = word.strip(string.punctuation)
        if word:
            query_words.append(word)

    print(f"Words after normalizing: {query_words}\n")
    res_docs = []
    res_docs_tf_idf = {}

    for word in query_words:
        # calculate_idf(word, total_pages, index)
        docs_list = index.get(word, [])
        # print(f"DOCS LIST: {docs_list}\n")

        for page_id in docs_list:

            tf_idf = calculate_tf_idf(word, page_id, index, total_pages)

            if page_id not in res_docs_tf_idf:
                res_docs_tf_idf[page_id] = tf_idf
            else:
                res_docs_tf_idf[page_id] += tf_idf

        # res_docs.extend(docs_list)

    # Display the fetched pages
    # return res_docs

    # Sort the res_docs_tf_idf w.r.t to the values
    # For large dictionaries, importing itemgetter from Python's built-in operator module is faster than using a lambda expression
    sorted_res_docs_tf_idf = dict(
        sorted(res_docs_tf_idf.items(), key=itemgetter(1), reverse=True)
    )

    return sorted_res_docs_tf_idf
