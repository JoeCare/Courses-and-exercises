from random import *


# DRAWING FUNCTIONS:

def printer(picture1,picture2,intgr):
    picture1[:intgr] = picture2[:intgr]
    for part in picture1:
        print(part)


def alter(pic1, pic2, scores, starting):
    current_score = starting - scores
    modifier = starting/5
    current_score *= modifier
    # procent = (current_score * starting) * 0.1
    print(current_score)
    lines1 = pic1.split('\n')
    lines2 = pic2.split('\n')
    if current_score == 0:
        printer(lines1, lines2, 0)
    elif 0 > current_score <= 1:
        printer(lines1, lines2, 1)
    elif 1 > current_score <= 2:
        printer(lines1, lines2, 2)
    elif 2 > current_score <= 3:
        printer(lines1, lines2, 3)
    elif 3 > current_score <= 4:
        printer(lines1, lines2, 4)
    elif 4 > current_score <= 5:
        printer(lines1, lines2, 5)


hanger = ". . . . . . . . .\n. . .  _-_  . . .\n. . . `  /  . . .\n" \
         ". ._____|_____. .\n./______.______\.\n. . . . . . . . .\n"
background = ". . . . . . . . .\n. . . . . . . . .\n. . . . . . . . .\n" \
             ". . . . . . . . .\n. . . . . . . . .\n. . . . . . . . .\n"

print(f'   WELCOME IN     \nTHE HANGING QUESTION\n{hanger}'
      f'Purpose of the game is to guess hidden word... before You got hanged!\n'
      f'In every turn You may ask for the letter - if hidden word includes it,\n'
      f'then it will be revealed to You but If isn\'t - You\'re one step closer to being hanged!\n'
      f'In every turn You can also try to decipher a whole riddle at once. Every puzzle is\n'
      f'one noun from English language. To make it easier not to get hanged in the closet\n'
      f'You may also get the hint about the category of the word.\n  GOOD LUCK!')


category = {
    1: ["anaconda", "crocodile", "hippo", "giraffe"],
    2: ["Predator", "Terminator", "Alien", "Titanic"],
    3: ["muffin", "tomato", "spaghetti", "cheesecake"]
}

animals = category.get(1)
movies = category.get(2)
edibles = category.get(3)


def rand_word():
    x = randrange(1,4)
    y = randrange(0,4)
    draw_cat = category.get(x)
    if x == 1:
        print("Category: animals.")
    elif x == 2:
        print("Category: movies.")
    else:
        print("Category: edibles.")
    draw_word = draw_cat[y]
    return draw_word


secret_word = rand_word()

hidden = []
w = len(secret_word)
for i in range(w):
    hidden.append("_")

score = w // 1.5
start = score
while score > 0:
    alter(background,hanger,score,start)

    print("SECRET WORD: ", " ".join(hidden))
    answer = input(f"Trials left: {int(score)}\nWant to guess the word [w],"
                   f"\nor need a letter [l] first?")
#    turn(answer)
    if answer == "w":
        haslo1 = input("Enter the word: ")
        if haslo1 == secret_word:
            print(f"Great guess! {secret_word.capitalize()} it is.\nCongratulations! You won the hanger,"
                  f"and there is no need to hide in the closet with it.")
            break
        else:
            print("Hell yeah! You are so wrong with that!")
            score -= 1
            continue
    elif answer == "l":
        print(" ".join(hidden))
        letter1 = input("Which letter? ")
        if letter1 in secret_word:
            lhaslo = list(enumerate(secret_word))
            for l in lhaslo:
                if letter1 in l:
                    x = l[0]
                    y = l[1]
                    hidden[x] = y
                else:
                    continue
        else:
            print(f'There is no "{letter1}" in the secret word.\n')
            score -= 1
    else:
        print("Missclick? Please try:\n w:\nOR\n l:")

        # answer = input("Typing error? Please enter:\nw:\nOR\nl:")
        # if answer == "h":
        #     haslo1 = input("Pass the word: ")
        #     if haslo1 == secret_word:
        #         print(f"You've got the word! {secret_word} it is.\nCongratulations! You won the hanger,"
        #               f"and there is no need to hide in the closet with it.")
        #         break
        #     else:
        #         print("Unfortunately not that one...")
        #         score -= 1
        #         continue
        # elif answer == "l":
        #     print("SECRET WORD:", " ".join(hidden))
        #     letter1 = input("Pick Your letter: ")
        #     if letter1 in secret_word:
        #         lhaslo = list(enumerate(secret_word))
        #         for l in lhaslo:
        #             if letter1 in l:
        #                 x = l[0]
        #                 y = l[1]
        #                 hidden[x] = y
        #             else:
        #                 continue



print(f"\n{hanger}\n     GAME OVER!\nHope You like it anyway!\n"
      f"You can take Your hanger and go hide in the closet.")