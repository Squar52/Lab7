n = int(input("Введіть кількість слів: "))

words = []

for i in range(n):
    word = input("Введіть слово: ")
    words.append(word)

count = 0

for i in range(n):
    for j in range(i + 1, n):
        if words[i][0] == words[j][0]:
            count += 1

print("Скільки пар слів з однаковою першою буквою:", count)