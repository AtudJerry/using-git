from timeit import timeit
sentence = "This is a common interview question"
dictionary = {}
for char in sentence:
    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1

final = (sorted(dictionary.items(), key=lambda kv:kv[1], reverse=True))
print(final[0])
print(dictionary)



