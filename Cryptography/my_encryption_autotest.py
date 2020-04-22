#!/usr/bin/env python3

# Thanks to Al Sweigart for this and many other Python exercises and projects ideas

# Because I wanted to code by myself as much as possible to avoid temptation
# for cheating and just copying I scrupulously omitted large parts of the book...
# simultaneously having about zero knowledge in the cryptography field.
# In consequence, excited about encrypting my messages, I didn't knew i.a that
# the crucial for hacking-resistance is the key... I introduced completely
# redundant tricks (like .replace(" ","%") - because cipher without spaces seemed to look
# more spectacular...) and then wasted a lots of time in other parts of project (my_hacker, encryption_autotest)
# dealing with them. Maybe I learned even more because of that, maybe not... but remember...
"""
A cipher is secure only if everything but the key can be revealed while still keeping the message a secret.
You cannot rely on a cryptanalyst’s not having access to the same encryption software or not knowing which cipher you used.
Always assume that the enemy knows the system!
"""
# ~Al Sweigart, "Cracking codes with Python"


import random
from my_decrypter import affine_decrypter
from my_encrypter import affine_cipher, check_valid_key1


def main():
    for example in random_strings(30):
        print(f'Original: {example}')
        keys = check_valid_key1(len(example) - 1, example)
        keyA = int((keys[random.randint(2, len(keys) - 1)]))
        keyB = random.randint(2, len(example) - 1)
        print(f'From {len(keys)} possibilities randomly picked {keyA} for primary key value and {keyB} for secondary.\n'
              f'All possibles were: {keys}')
        encrypted_example = affine_cipher(keyA, keyB, example)
        print(f'Encrypted: {encrypted_example}')
        decrypted_back = affine_decrypter(keyA, keyB, encrypted_example)
        print(f'Decrypted: {decrypted_back}')
        if example == decrypted_back:
            continue
        else:
            raise Exception(f'Encryption not proper with 1th key {keyA} and 2nd key {keyB}.')
    return "Encryption correct."


def random_strings(number):  # TRANSLATE IT TO GENERATOR LATER
    random_messages_set = []
    random.seed(3)
    for n in range(number):
        string = "ABCDEFGHIJKLMNOPQRSTUWXYZ " * random.randint(2, 12)
        string = list(string)
        random.shuffle(string)
        string = ''.join(string)
        random_messages_set.append(string)
    return random_messages_set


if __name__ == '__main__':
    main()
