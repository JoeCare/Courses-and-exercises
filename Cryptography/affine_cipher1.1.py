#!/usr/bin/env python3

# AFFINE CIPHER:
# thanks to Al Sweigart for this and many other Python exercises and projects ideas


def main():
    user_msg = input('Please type or paste string You want to encrypt. Percent sign "%" is forbidden.')
    key1_possibilities = check_valid_key1(100,user_msg)
    key1 = int(input(f'Please input first encryption key value for Your message. '
                     f'It`s recommended to choose one from below:'
                     f'\n{",".join(key1_possibilities)}'))
    key2 = int(input(f'Please input second encryption key. It should be number between 2 and {len(user_msg)}'))
    encrypted_msg = affine_cipher(key1,key2,user_msg)
    # # chars_and_nums = [i for i in enumerate(oryginal_msg)]
    # # to print full set numeration for calculations above and comparison
    # # print(chars_and_nums)
    print(f'{user_msg}\nYour text has been encrypted with {key1} set as 1th Key and {key2} as 2nd Key value.\n'
          f'Remember! Those numbers are necessary for future decryption.\n{encrypted_msg}')


def gcd(a,b):
    """Finding greatest common divisor. Whole function copied from Al Sweigart website."""
    while a != 0:
        a, b = b % a, a
    return b


# My own work:
def check_valid_key1(value_range, char_set):
    """Check in specified range for valid keys (relatively prime to characters set size)."""
    possible_keys = []
    num = 2
    while num < value_range:
        if gcd(num,len(char_set))==1:
            possible_keys.append(str(num))
            num += 1
        num += 1
    return possible_keys


def affine_cipher(key1_value, key2_value, char_str):
    encryption = []
    # encryption1 = []
    for n, char in enumerate(char_str):
        encr_n = ((n * key1_value) + key2_value) % len(char_str)
        # symbol = encr_n, char_str[encr_n]
        # encryption1.append(symbol)  # for returning list of tuples like with enumerate function
        encryption.append(char_str[encr_n])
    encrypted_str = ''.join(encryption).replace(" ","%")
    # print(char_str)
    # print(encrypted_str)  # for comparison
    # print(encryption1)
    return encrypted_str


if __name__ == '__main__':
    main()
