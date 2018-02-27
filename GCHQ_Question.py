import enchant
import string
import random
dic = enchant.Dict("en_UK")
alphabet = list(string.ascii_lowercase)


def word_builder(word, length=5):
    alpha = alphabet.index(word[-1:]) + 1
    if len(word) > length:
        return word
    elif alpha >20:
        return word + alphabet[alpha + random.randint(0,25 - alpha)]
    # print(alpha)

    else:
        return word_builder(word + alphabet[alpha + random.randint(0,4)])


prefixes = ["a","b","c","d","e","f","g","h"]
sizes = range(5,8)

for prefix in prefixes:
    best_final = ""
    for size in sizes:

        for i in range(10000):

            garble = word_builder(prefix, length=size)
            if dic.check(garble) == True:
                if (len(garble) >= len(best_final)):
                    best_final = garble

    print(best_final)


