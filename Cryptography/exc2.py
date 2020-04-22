# AFFINE CIPHER:
# thanks to Al Sweigart for those and many other Python exercises ideas
# http://inventwithpython.com/cracking/chapter13.html

def gcd(a,b):
    """Finding greatest common divisor. Function copied from Al Sweigart website."""
    while a != 0:
        a, b = b % a, a
    return b


# My own work:

def check_valid_keys(value_range, char_set):
    """Check in specified range for valid keys"""
    keys = []
    num = 1
    while num < value_range:
        if gcd(num,len(char_set))==1:
            keys.append(num)
            num += 1
        num += 1
    return keys


def multiplication_cipher(key_value, char_set):
    encryption = []
    encryption1 = []
    for n, char in enumerate(char_set):
        encr_n = (n*key_value) % len(char_set)
        symbol = encr_n, char_set[encr_n]
        encryption1.append(symbol)  # for returning list of tuples like with enumerate function
        encryption.append(char_set[encr_n])
    encrypted_set = ''.join(encryption)
    print(char_set)
    print(encrypted_set)  # for comparison
    print(encryption1)
    return encrypted_set


oryginal_msg = 'I love Alex!'
multiplication_cipher(17,oryginal_msg)
chars_and_nums = [i for i in enumerate(oryginal_msg)]
# to print full set numeration for calculations above and comparison
print(chars_and_nums)

