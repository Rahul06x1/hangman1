import random

def get_random_word(wordlist="/usr/share/dict/words"):
    global unmasked
    good_words = []
    with open(wordlist) as f:
        words = [x.strip() for x in f]
        for word in words:
            if not word.isalpha(): # if there is punctuation
                continue
            if not word.islower(): # if it is a proper noun
                continue
            if len(word) < 5: # Too short
                continue
            good_words.append(word)

        unmasked = random.choice(good_words)
        return unmasked
    
def mask_secret_word(unmasked = get_random_word()):
    global masked
    masked = len(unmasked)*"-"
    return masked

def get_user_input(user_input):
    if len(user_input) == 1:
        return user_input
    else:
        get_user_input(input('Enter only one charactor: '))
