import random

def get_random_word(wordlist="/usr/share/dict/words"):
    global secret_word
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

        secret_word = random.choice(good_words)
        return secret_word
    
def mask_secret_word(secret_word = get_random_word()):
    global masked
    masked = len(secret_word)*"-"
    return masked

def get_user_input(user_input):
    global temp_user_input
    if len(user_input) == 1:
        temp_user_input = user_input
        return temp_user_input
    else:
        print(masked,secret_word)
        get_user_input(input('Enter only one charactor: '))

def check_user_input_secret_word(user_input, secret_word):
    # mask_secret_word(secret_word)
    print(masked,'kkk')
    if user_input in secret_word:
        position = [
            index for index, item in enumerate(secret_word)
            if item == user_input
            ]
        list_masked = list(masked)
        for p in position:
            list_masked[p] = user_input
        masked = ''.join(list_masked) 
        # change_global_masked(''.join(list_masked) ) 
        print('pos',position)
        print('mas',masked)
        print('uma',secret_word)

        return user_input

def main():
    # masked = 'temp'
    mask_secret_word(secret_word)
    print(masked,secret_word)
    user_input = input('Enter only one charactor: ')
    get_user_input(user_input)
    check_user_input_secret_word(temp_user_input,secret_word)

if __name__ == '__main__':
    main()
