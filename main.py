from pathlib import Path
import string

documents_path = Path("documents")

for file in documents_path.iterdir():

    content = file.read_text()

    print("=" * 40)
    print(file.name)
    # print(content)

    words = content.split()
    for word in words:
        word = word.lower()
        word = word.strip(string.punctuation)
        print(word)
