text = input("Ввести декілька слів: ")

words = text.split()

words.sort(key=len, reverse=True)

print("Слова від найдовшого до найкоротшого:")

for word in words:
    print(word)