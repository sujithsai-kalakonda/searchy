import string

def search(query: str, index: dict):
    # split and normalize the query
    query_words = []

    for word in query.split():
        word = word.lower()
        word = word.strip(string.punctuation)
        if word:
            query_words.append(word)

    print(f"Words after normalizing: {query_words}\n")
    res_docs = []

    for word in query_words:
        docs_list = index.get(word, [])
        # print(f"DOCS LIST: {docs_list}\n")
        res_docs.extend(docs_list)

    # Display the fetched pages
    return res_docs