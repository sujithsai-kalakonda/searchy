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
    res_docs_dict = (
        {}
    )  # this dict contains doc names and how many times it occurs in the res_docs
    for word in query_words:
        docs_list = index.get(word, [])
        res_docs.extend(docs_list)

        for doc in docs_list:
            if doc in res_docs_dict:
                res_docs_dict[doc] += 1
            else:
                res_docs_dict[doc] = 1

    # Sort the dict w.r.t to count
    sorted_res_docs_dict = dict(
        sorted(res_docs_dict.items(), key=lambda item: item[1], reverse=True)
    )

    # print("Total Docs list", res_docs)
    # print("Total Docs map-1", sorted_res_docs_dict)
    # print("-" * 50)

    return sorted_res_docs_dict


def main():
    print("========================")
    print("       SEARCHY 🔎       ")
    print("========================")

    while True:
        query = input("Type your query: ")
        if query.lower().strip() == "exit":
            print("GoodBye 👋....")
            return

        print("searching.....")

        res = search(query)
        if res:
            for idx, key in enumerate(res):
                print(f"{idx+1}. {key}")
                print(f"   Score: {res[key]}")
                print()
        else:
            print("OOPS! No result found....")
            print()


if __name__ == "__main__":
    main()
