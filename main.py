from pathlib import Path
import string

documents_path = Path("documents")

# This dict contains words and documents list which contains that words
index = {}

for file in documents_path.iterdir():

    content = file.read_text()

    print("=" * 40)
    print(file.name)
    # print(content)

    # Text -> words
    words = content.split()
    for word in words:

        # normalize
        word = word.lower()
        word = word.strip(string.punctuation)
        # print(word)

        if word:
            # avoid adding empty string
            if word not in index:
                index[word] = []

            # Also make sure the same document is not appended twice.
            if file.name not in index[word]:
                index[word].append(file.name)

print(index)


def search(query: str):
    # split and normalize the query
    query_words = []

    for word in query.split():
        word = word.lower()
        word = word.strip(string.punctuation)
        if word:
            query_words.append(word)

    res_docs = []
    for word in query_words:
        docs_list = index.get(word, [])
        res_docs.extend(docs_list)

    print("Total Docs list", res_docs)
    print("-" * 50)

    return res_docs


search("python")

search("tcp")

search("elephant")

search("python networking")

search("physical stack")
