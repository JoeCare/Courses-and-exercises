# BRUTE-FORCE HACKING ON AFFINE ENCRYPTION
# thanks to Al Sweigart for great inspiration to learn Python every damn evening for...

from almodules import affineCipher, detectEnglish, cryptomath
from Cryptography import affine_decipher as deciph


def hack_affine(ciphered_str):
    input('Press Ctrl+D to abort at any time. Press any key to continue.')
    print("Starting process...")
    # ...called brute-force hacking
    # possible_key1 = []
    # possible_key2 = []
    possible_decryption = ["Nothing yet."]
    while len(possible_decryption) > 0:
        for key2 in range(len(ciphered_str)):
            # print(key2)
            # possible_key2.append(key2)
            for key1 in range(len(ciphered_str)):
                if deciph.gcd(key1,len(ciphered_str)) == 1:
                    # print(key1)
                    # possible_key1.append(key1)
                    descr = deciph.affine_decipher(key1,key2,ciphered_str)
                    possible_decryption.append(descr)
                    # print(descr)
        for deciphred in possible_decryption:
            if detectEnglish.isEnglish(deciphred):
                print(deciphred)
                response = input("May it be the message? Any key to continue.\n"
                                 "Press 'd' to delete string.\n"
                                 "Press 's' to stop - encryption found.\n")
                if response == 'd':
                    possible_decryption.remove(deciphred)
                elif response == 's':
                    print(f'Your message is: {deciphred}')
                    return deciphred
                else:
                    continue
            else:
                possible_decryption.remove(deciphred)


msg = '5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu'

hack_affine(msg)


