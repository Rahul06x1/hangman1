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

        secret_word = random.choice(good_words)
        return secret_word
    
def mask_secret_word(secret_word):
    masked = len(secret_word)*"-"
    return masked

def get_user_input(masked,guessed_word):
    print(masked)
    user_input = input('Enter only one charactor: ')
    if len(user_input) == 1:       
        if user_input in guessed_word:
            print('Input already guessed')
            get_user_input(masked, guessed_word)
        else:
            guessed_word.append(user_input)
        print("Guessed Words: ","'","".join(guessed_word),"'")
        return user_input, guessed_word
    else:
        get_user_input(masked, guessed_word)

def check_user_input_secret_word(user_input, secret_word,masked,chance):
    if user_input in secret_word:
        position = [
            index for index, item in enumerate(secret_word)
            if item == user_input
            ]
        list_masked = list(masked)
        for p in position:
            list_masked[p] = user_input
        masked = ''.join(list_masked) 
    else:
        chance -= 1
    return user_input, masked, chance

def main():
    guessed_word = []
    secret_word = get_random_word(wordlist="/usr/share/dict/words")
    masked = mask_secret_word(secret_word)
    chance = len(secret_word)
    while masked != secret_word:
        if chance == 0:
            print('Game Over. You lose.')
            break
        print("You have ", chance, 'chances')
        user_input, guessed_word = get_user_input(masked, guessed_word) 
        user_input, masked, chance = check_user_input_secret_word(user_input,secret_word,masked,chance)
        if masked == secret_word:
            print('You Won')
            break
    play_again_condition = input('Do you want to play again? [Y/N]')
    if play_again_condition.lower() == 'y':
        main()

        
if __name__ == '__main__':
    main()
