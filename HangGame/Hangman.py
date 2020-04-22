from random import *

"""
Hangman

The Goal: Despite the name, the actual “hangman” part isn’t necessary.
The main goal here is to create a sort of “guess the word” game.
The user needs to be able to input letter guesses.
A limit should also be set on how many guesses they can use.
This means you’ll need a way to grab a word to use for guessing.
(This can be grabbed from a pre-made list. No need to get too fancy.)
You will also need functions to check if the user has actually inputted a single letter,
to check if the inputted letter is in the hidden word (and if it is, how many times it appears),
to print letters, and a counter variable to limit guesses.
Concepts to keep in mind:

Random Variables Boolean
Input and Output Integer
Char String Length Print
"""
w0 = ". . . . . . . . . \n. . . . C . . . .\n. . . __|__ . . .\n. . /. . . .\ . .\n. ./_________\. .\n. . . . . . . . .\n"


print("ZAPRASZAMY DO GRY:\n     WIESZAK!\n"+w0, "Celem gry jest odgadnięcie słowa o podanej liczbie liter.\n"
                                                 "Gracz w każdej próbie może podjąć się odgadnięcia hasła, lub wskazać (w późniejszych wersjach kupić,\n"
                                                 "za kwotę zależną od tego czy to samogłoska(drozsze) czy spółoska) literę do odkrycia. Jeśli litera znajduje się w slowie, to stana sie jawne wszystkie jej wystapienia.\n"
                                                 "jeśli nie - gracz traci jedną szanę.\n")


def hanger():
    hanger1 = []
    for line in w0.split('\n'):
        hanger1.append(line)
        # print(line)
    return hanger1

func1 = hanger()


def plain_backgroung():
    list1 = ['.']*9
    plain = [x for x in list1]
    line1 = ' '.join(plain)
    background = []
    for line in range(0,6):
        background.append(line1)
    # for line in hanger:
    #     print(line)
    return background


background = plain_backgroung()


def hanger_animation(function, background,starting,current):
    if starting == current:
        for line in background:
            print(line)
    elif starting == current+1:
        change = current - starting
        background.insert(change,function[change])
        for line in background:
            print(line)






haslo = randrange(1, 3)
if haslo == 1:
    haslo = "dinozaur"
elif haslo == 2:
    haslo = "żyrafa"
elif haslo == 3:
    haslo = "trawa"
elif haslo == 4:
    haslo = "tabakierka"
elif haslo == 5:
    haslo = "rewolwer"
else:
    print("Error w chuj")

niewidoczne = []
w = len(haslo)
for i in range(w):
    niewidoczne.append("_")

count = w // 2
start_count = count
current_count = count

# def gen_word():
#     x = randrange(1, 5)
#     if x == 1: return "prestidigitator"
#     elif x == 2: return "marchew"
#     elif x == 3: return "trawa"
#     elif x == 4: return "tabakierka"
#     elif x == 5: return "rewolwer"
#     else:
#         print("Error w chuj")
#     albo ->


#
# def char_check(niewidoczne, haslo, litera1):
#         if litera1 in haslo:
#             lhaslo = list(enumerate(haslo))
#             for l in lhaslo:
#                 if litera1 in l:
#                     return l[0]
#                 else:
#                     continue


#
# def turn(answer):
#     if answer == "haslo":
#         haslo1 = input("Podaj haslo: ")
#         return haslo1
#     elif answer1 == "litera":
#         litera1 = input("Jaka? ")
#         return litera1
#     else:
#         print("Proszę wpisać:\nhasło\nlub:\nlitera")
#         return turn()

# def check_win(turn):
#     if turn == haslo1:
#



for gra in range(count):

    print("HASŁO: ", " ".join(niewidoczne))
    answer = input(f'Pozostało prób: {count} \nOdgadujesz hasło[h],'
                   f' czy chcesz wskazać literę[l] do odkrycia?: ')
    #    turn(answer)
    if answer == "h":
        haslo1 = input("Podaj haslo: ")
        if haslo1 == haslo:
            print(f"Odgadłeś hasło: {haslo} \nMAMY ZWYCIĘSCE!")
            break
        else:
            print("Błędne hasło!")
            count -= 1
            hanger_animation(func1, background, start_count, count)
            continue
    elif answer == "l":
        print(" ".join(niewidoczne))
        litera1 = input("Jaka litera? ")
        if litera1 in haslo:
            lhaslo = list(enumerate(haslo))
            for l in lhaslo:
                if litera1 in l:
                    x = l[0]
                    y = l[1]
                    niewidoczne[x] = y
                else:
                    continue
        else:
            print(f'Hasło nie zawiera litery "{litera1}".\n')
            # hanger_animation(count)
    else:
        answer = input("Błąd wprowadzania! Proszę wpisać:\nh:\nlub\nl:")
        if answer == "h":
            haslo1 = input("Podaj haslo: ")
            if haslo1 == haslo:
                print("Odgadłeś hasło: {} \nMAMY ZWYCIĘSCE!".format(haslo))
                break
            else:
                print("Błędne hasło!")
                count -= 1
                hanger_animation(func1, background, start_count, count)
                continue
        elif answer == "l":
            print("HASŁO:", " ".join(niewidoczne))
            litera1 = input("Jaka? ")
            if litera1 in haslo:
                lhaslo = list(enumerate(haslo))
                for l in lhaslo:
                    if litera1 in l:
                        x = l[0]
                        y = l[1]
                        niewidoczne[x] = y
                    else:
                        continue
            else:
                print('Hasło nie zawiera litery "{}"\n\n'.format(litera1))
        else:
            answer = input("Błąd wprowadzania! Proszę wpisać:\nh:\nlub\nl:")
            if answer == "h":
                haslo1 = input("Podaj haslo: ")
                if haslo1 == haslo:
                    print("Odgadłeś hasło: {} \nMAMY ZWYCIĘSCE!".format(haslo))
                    break
                else:
                    print("Błędne hasło!")
                    count -= 1
                    hanger_animation(func1, background, start_count, count)
                    continue
            elif answer == "l":
                print(" ".join(niewidoczne))
                litera1 = input("Jaka? ")
                if litera1 in haslo:
                    lhaslo = list(enumerate(haslo))
                    for l in lhaslo:
                        if litera1 in l:
                            x = l[0]
                            y = l[1]
                            niewidoczne[x] = y
                        else:
                            continue
    count -= 1
    hanger_animation(func1, background, start_count, count)

print(f'KONIEC GRY. Poszukiwanym słowem było: "{haslo}"')
