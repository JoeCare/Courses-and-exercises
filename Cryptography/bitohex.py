# Binary to Hexadecimal converter
# What does it mean system is 32 or 64-bit?
# One bit is information of the value 0 or 1: two possibilities.
# In hexadecimal notation which gives 16 possibilities we need 4 bits:
# because 2^4 = 16.

binary = "0101110011100011001010"  # input("Type a binary string.")
binary_list1 = list(binary)
# binary_list1.reverse()
# rbinary = str(binary_list1)
# binary_list1.reverse()
binary_list2 = []

rbinary = ""
rbinary2 = ""
if len(binary_list1) > 4:
    binary_list1.reverse()
    rbinary = "".join(binary_list1)
    print(rbinary)
    for index in range(0, len(rbinary)-1, 4):
        # if index <= len(rbinary)-1:
        binary_list2.append(rbinary[index : index + 4])
    rbinary2 = "".join(binary_list2)

binary_list2.reverse()
print(binary_list2, rbinary2)
for list in binary_list2:
    for n in list:
        pass



