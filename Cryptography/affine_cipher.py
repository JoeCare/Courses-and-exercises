# AFFINE CIPHER:
# thanks to Al Sweigart for this and many other Python exercises and projects ideas
# http://inventwithpython.com/cracking/chapter13.html


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


def affine_cipher(key1_value, key2_value, char_str):
    encryption = []
    encryption1 = []
    for n, char in enumerate(char_str):
        encr_n = ((n * key1_value) + key2_value) % len(char_str)
        symbol = encr_n, char_str[encr_n]
        encryption1.append(symbol)  # for returning list of tuples like with enumerate function
        encryption.append(char_str[encr_n])
    encrypted_str = ''.join(encryption)
    # print(char_str)
    # print(encrypted_str)  # for comparison
    # print(encryption1)
    return encrypted_str


def affine_decipher(key1_value, key2_value, ciphred_str):
    mod_inv = find_modular_inverse(key1_value, ciphred_str)
    decryption = []
    for n, char in enumerate(ciphred_str):
        decr_n = ((n-key2_value)*mod_inv)%len(ciphred_str)
        decryption.append(ciphred_str[decr_n])
    # print(decryption)
    decrypted_str = ''.join(decryption)
    return decrypted_str


oryginal_msg = 'I would like to eat a peach.'
print(check_valid_key1(50,oryginal_msg))
encrypted_msg = affine_cipher(23,6,oryginal_msg)
# # chars_and_nums = [i for i in enumerate(oryginal_msg)]
# # to print full set numeration for calculations above and comparison
# # print(chars_and_nums)
print(oryginal_msg)
print(encrypted_msg)
print(affine_decipher(23,6,'d a oiu.pa  wca klIettloh ee'))
