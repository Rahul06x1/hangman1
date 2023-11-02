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
    global temp_user_input
    if len(user_input) == 1:
        temp_user_input = user_input
        return temp_user_input
    else:
        print(masked,unmasked)
        get_user_input(input('Enter only one charactor: '))

def check_user_input_secret_word(user_input, unmasked):
    if user_input in unmasked:
        return user_input

def main():
    mask_secret_word(unmasked)
    print(masked)
    user_input = input('Enter only one charactor: ')
    get_user_input(user_input)
    check_user_input_secret_word(temp_user_input,unmasked)

if __name__ == '__main__':
    main()
