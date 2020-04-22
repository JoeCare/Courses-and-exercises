# MULTIPLICATIVE CIPHER:
# thanks to Al Sweigart for those and many other Python exercises ideas
# http://inventwithpython.com/cracking/chapter13.html

"""
Imagine clock with 0 hour over 12 and put aside PM/AM case.
Let's say we've got 5 o`clock - what time will be after 4 hours?
5+4=9, so it will be nine o`clock. And what hour will be after next 8 hours?
9+8=17... but we don't have 17 hour on the clock. So we have to substract 12
counting one full turn of our clock (with real data it would mean that its day+1 or change from AM to PM etc.)
17-12=5 we've got five o`clock - good time for a tea.
What if we would like to point out what hour will be after 300 next hours?
5+300=305 and we obviously don`t have such hour so lets substract 12
305-12=293 still nothing suitable for the clock...
We should to substract 12 until we get number between 0 and 12 - to point out on our clock.
Every time we make full turn around clock face it would be another day(AM) or night(PM) cycle
But it still doesnt matter - it means, after those long nights, we'll have our clock indicate
hour that we were looking for. It will be 5. How I know this.
Thanks to modulo operator of modular arithmetic.
305%12=5, also 305/12=25.416 and 12*25.416=304.992~305
It means after there is 25 times 12 in 300, and then 5 stays - its our hour like before, first which is
less than 12.
Equation for our future hour would be (present_hour_number+add_hours_number)%max_hour_number.
print(17%12, 305%12)
So modulo operation is simply reminder of division i-number by j-number;
Obviously numbers which divide evenly modulo=0. It its usable i.a. to find greatest common divisor.
"""

# Multiple assigning and swaping values
a, b, c = 1, 'hello', 4
print(a,b,c)
# >>>1 hello 4
foo = 'yo'
hoo = 'bye'
foo, hoo = hoo, foo
print(foo,hoo)
# >>>bye yo
# after asigning yo to foo, and bye to hoo, we assign hoo ('bye') to foo, and foo('yo') to hoo - values swapped


def gcd(a,b):
    """Finding greatest common divisor"""
    while a != 0:
        a, b = b % a, a
    return b
# this math has 2k years and I still didn't had a time to learn it -.
# Yeah... So... Lets take 12 and 32, a=12, b=32
# cuz 12 is not 0 we enter the loop
# now we assigning new values:
# a = b%a, so a=32%12; b=a, so b=12
# 32%12=8, so a=8, b=12; 8 is not 0 so loop iterates again
# a=12%8, b=8; 12%8=4, so a=4 and its not 0 - means another loop
# a=8%4, b=4; 8%4=0, because 4 is 2 times in 8 without reminder; a=0, b=4
# function returns 4 as greatest common divisor


print(gcd(12,32))
# >>>4
# advance of this function is it works for large numbers as well
print(gcd(34524326, 7890871))
# >>>29
print(34524326/29, 7890871/29)
# >>>1190494.0 272099.0 - it divides without reminder so its proper divisor
# gcd() function may be used to choose keys for affine and multiplicative cipher

# MULTIPLICATION CIPHER:
# but first... here is the encryption with famous Caesar cipher (completely useless?):
standard_alphanum = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
caesar_encryption = 'RSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.ABCDEFGHIJKLMNOPQ'
# every char is just moved 49 chars further
# ____unimportant trials for nice table view with lists printing
# standard_alphanum2 = [i+' ' for i in standard_alphanum if len(i)==1]
# nums_for_alphanum2 = [str(i) for i,c in enumerate(standard_alphanum)]
# print(f'{standard_alphanum2}\n{nums_for_alphanum2}')

standard_alphanum1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
mulip_with_17_encr = 'ARizCTk2EVm4GXo6IZq8Kbs0Mdu!Ofw.QhyBSj1DUl3FWn5HYp7Jar9Lct Nev?Pgx'
# standard_alphanum3 = [i for i in standard_alphanum1]
# mulip_with_17_enc3 = [i for i in mulip_with_17_encr]
# print(f'{standard_alphanum3}\n{mulip_with_17_enc3}')  # for better view to compare sets
# here we immediately see much more randomization due to oryginal set - its because modulo operation:
# multiplicative cipher is made with Key which means that
# number 0-65 assigned for specific character is multiplicated by Key value - i.e. 17
# for E-4 it would be 4*17=68 and than we mod it by 66-max number, 68%66 gives us 2-C;
# without modulo operator 68 would indicate to second sign B, so it would simply wraparound
# like in Caesar Cipher

# RIGHT KEY:

# Yet its not completely free to choose number for the Key value in that cipher
# let's take 11 for G-6: (6*11)%66=0; for M-12: (12*11)%66=0; same for A, N, F, S etc...
# such encryption is impossible to decrypt and obviously useless - noone could recognize from which
# particular character originally were all those As ciphered;
# to avoid it we must be sure that Key value and character set length must be relatively prime
# which means their greatest common divisor is 1;
# they don't have to be prime numbers to be relatively prime to each other!


def multiplication_cipher(key_value, char_set):
    encryption = []
    encryption1 = []
    for n, char in enumerate(char_set):
        encr_n = (n*key_value) % len(char_set)
        symbol = encr_n, char_set[encr_n]
        encryption1.append(symbol)  # for returning list of tuples like with enumerate function
        encryption.append(char_set[encr_n])
    encrypted_set = ''.join(encryption)
    print(encryption1)
    # print(char_set)
    # print(encrypted_set)  # for comparison
    return encrypted_set


def multiplication_decipher(key_value, ciphred_str):
    pass


# multiplication_decipher(17,'ARizCTk2EVm4GXo6IZq8Kbs0Mdu!Ofw.QhyBSj1DUl3FWn5HYp7Jar9Lct Nev?Pgx')


def check_valid_keys(value_range, char_set):
    """Check in specified range for valid keys"""
    # DON'T KNOW IF IT WORK CORRECTLY
    keys = []
    num = 1
    while num < value_range:
        if gcd(num,len(char_set))==1:
            keys.append(num)
            num += 1
        num += 1
    return keys


# print(check_valid_keys(100,standard_alphanum), len(standard_alphanum))
# function for keys


multiplication_cipher(17,standard_alphanum)
chars_and_nums = [i for i in enumerate(standard_alphanum)]
# to print full set numeration for calculations above and comparison
print(chars_and_nums)

print(17%)