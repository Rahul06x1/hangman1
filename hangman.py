import random

def get_random_word(wordlist="/usr/share/dict/words"):
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

        return random.choice(good_words)
    
def mask_secret_word(unmasked = get_random_word()):
    masked = len(unmasked)*"-"
    return masked

def get_user_input(user_input):
    if len(user_input) == 1:
        return user_input

print(get_user_input('s'))
