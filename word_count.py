with open("sample.txt", "r", encoding="utf-8")as f:
    text = f.read()

words = text.split()

print("words count: ", len(words))