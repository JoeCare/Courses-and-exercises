from random import *

"""dodac info ze taka litera juz byla"""
"""kiedy zwycierzasz po literze to nie ma komunikatu"""
"""jak skoncza sie szanse to nie wyswietla sie ze porazka + haslo jakie bylo"""


# ANIMATING FUNCTIONS:

def printer(picture1,picture2,intgr):
    picture1[:intgr] = picture2[:intgr]
    for part in picture1:
        print(part)


# def printer1(picture1,picture2,intgr):
#     picture1[intgr] = picture2[intgr]
#     newpic = picture1
#     return newpic
# Another possible printer function

def alter(pic1, pic2, current_score):
    # starting_score = score
    # current_score = starting_score - score
    lines1 = pic1.split('\n')
    lines2 = pic2.split('\n')
    # new_pic = []
    if current_score <= 1:
        printer(lines1, lines2, current_score)
    elif current_score <= 2:
        printer(lines1, lines2, current_score)
    elif current_score <= 3:
        printer(lines1, lines2, current_score)
    elif current_score <= 4:
        printer(lines1, lines2, current_score)
    elif current_score <= 5:
        printer(lines1, lines2, current_score)


hanger = ". . . . . . . . .\n. . . .___. . . .\n. . . `  /  . . .\n" \
         ". ._____|_____. .\n. /_____._____\ .\n. . . . . . . . .\n"
background = ". . . . . . . . .\n. . . . . . . . .\n. . . . . . . . .\n" \
             ". . . . . . . . .\n. . . . . . . . .\n. . . . . . . . .\n"

alter(background,hanger,4)



# h_list = get_hanger()
#
#
# def get_ground(cur_score, list2):
#     length = 5 - cur_score
#     for line in range(0,length):
#         list2.insert(line,". . . . . . . . .")
#     return list2
#
# ground = get_ground(2,h_list)  # creates the ground[]


#
# def pic_print(score):
#     starting_score = score
#     current_score = starting_score - score
#     if current_score == 0:
#         for line in get_ground(0):
#             print(line)
#     elif current_score == 1:
#         for line in get_ground(1):
#             print(line)
#     elif current_score == 2:
#         for line in get_ground(2):
#             print(line)
#     elif current_score == 3:
#         for line in get_ground(3):
#             print(line)
#     elif current_score == 4:
#         for line in get_ground(4):
#             print(line)
#     elif current_score >= 5:
#         for line in get_ground(5):
#             print(line)



# HANGING QUESTION!

print("ZAPRASZAMY DO GRY:\n     WIESZAK!\n"+hanger ,"Celem gry jest odgadnięcie słowa o podanej liczbie liter.\n"
      "Gracz w każdej próbie może podjąć się odgadnięcia hasła, lub wskazać (w późniejszych wersjach kupić,\n"
      "za kwotę zależną od tego czy to samogłoska(drozsze) czy spółoska) literę do odkrycia. Jeśli litera znajduje się w slowie, to stana sie jawne wszystkie jej wystapienia.\n"
      "jeśli nie - gracz traci jedną szanę.\nHasla sa wylacznie w jezyku polskim, jednowyrazowe, bez polskich znaków.\n")

kategorie = {
    1: ["anakonda", "krokodyl", "hipopotam", "zyrafa"],
    2: ["Predator", "Terminator", "Obcy", "Titanic"],
    3: ["malwa", "bratek", "topola", "mydelnica"]
}

zwierzeta = kategorie.get(1)
filmy = kategorie.get(2)
rosliny = kategorie.get(3)



def rand_word():
    x = randrange(1,4)
    y = randrange(0,4)
    losujkategorie = kategorie.get(x)
    if x == 1:
        print("KATEGORIA: zwierzeta.")
    elif x == 2:
        print("KATEGORIA: filmy.")
    else:
        print("KATEGORIA: rosliny.")
    losujslowo = losujkategorie[y]
    return losujslowo

haslo = rand_word()

niewidoczne = []
w = len(haslo)
for i in range(w):
    niewidoczne.append("_")

score = w // 1.5

while score == 0:

    print("HASŁO: ", " ".join(niewidoczne))
    answer = input("Pozostało prób: {} \nOdgadujesz hasło[h], czy chcesz wskazać literę[l] do odkrycia?: ".format(int(score)))
#    turn(answer)
    if answer == "h":
        haslo1 = input("Podaj haslo: ")
        if haslo1 == haslo:
            print("Odgadłeś hasło: {} \nMAMY ZWYCIĘSCE!".format(haslo))
            break
        else:
            print("Błędne hasło!")
            score -= 1
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
            print('Hasło nie zawiera litery "{}".\n\n'.format(litera1))
            score -= 1
    else:
        answer = input("Błąd wprowadzania! Proszę wpisać:\nh:\nlub\nl:")
        if answer == "h":
            haslo1 = input("Podaj haslo: ")
            if haslo1 == haslo:
                print("Odgadłeś hasło: {} \nMAMY ZWYCIĘSCE!".format(haslo))
                break
            else:
                print("Błędne hasło!")
                score -= 1
                continue
        elif answer == "l":
            print("HASŁO:", " ".join(niewidoczne))
            litera1 = input("Wskaz litere: ")
            if litera1 in haslo:
                lhaslo = list(enumerate(haslo))
                for l in lhaslo:
                    if litera1 in l:
                        x = l[0]
                        y = l[1]
                        niewidoczne[x] = y
                    else:
                        continue

print("KONIEC GRY.")