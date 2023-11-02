import random

def get_random_word(wordlist="/usr/share/dict/words"):
    good_words = []
    with open(wordlist) as f:
        words = [x.strip() for x in f]
        for word in words:
            if not word.islower(): # if it is a proper noun
                continue
            good_words.append(word)

        return random.choice(good_words)