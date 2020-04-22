#!/usr/bin/env python3

# AFFINE DECIPHER:
# thanks to Al Sweigart for this and many other Python exercises and projects ideas


def main():
    user_msg = input('Please type or paste string You want to decrypt.')
    key1 = int(input('Please input first encryption key value for Your message.'))
    key2 = int(input('Please input second encryption key.'))
    decrypted_msg = affine_decipher(key1, key2, user_msg)
    # # chars_and_nums = [i for i in enumerate(oryginal_msg)]
    # # to print full set numeration for calculations above and comparison
    # # print(chars_and_nums)
    print(f'{user_msg}\nYour text has been decrypted:\n{decrypted_msg}')


def gcd(a,b):
    """Finding greatest common divisor. Whole function copied from Al Sweigart website."""
    while a != 0:
        a, b = b % a, a
    return b


def find_modular_inverse(encryption_key_value, char_set):
    a = encryption_key_value
    m = len(char_set)
    """Whole rest of that function is copied from Al."""
    if gcd(a, m) != 1:
        return None  # No mod inverse if a & m aren't relatively prime.
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3  # Note that // is the integer division operator.
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


# My own work:
def check_valid_key1(value_range, char_set):
    """Check in specified range for valid keys"""
    possible_keys = []
    num = 1
    while num < value_range:
        if gcd(num,len(char_set))==1:
            possible_keys.append(num)
            num += 1
        num += 1
    return possible_keys


def affine_decipher(key1_value, key2_value, ciphred_str):
    ciphred_str = ciphred_str.replace("%"," ")
    mod_inv = find_modular_inverse(key1_value, ciphred_str)
    decryption = []
    for n, char in enumerate(ciphred_str):
        decr_n = ((n-key2_value)*mod_inv)%len(ciphred_str)
        decryption.append(ciphred_str[decr_n])
    # print(decryption)
    decrypted_str = ''.join(decryption)
    return decrypted_str


if __name__ == '__main__':
    main()
