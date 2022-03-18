from sympy import isprime


def isitprime(k):
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k < 2:
        return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True


text = "The quick brown fox jumps over the lazy dog"
for word in text.split():
    print(word)

my_list = list(range(3, 43))
my_list_square = [i ** 2 for i in my_list]
print(my_list_square)

my_dict = {i: str(i) * 3 for i in my_list_square}
print(my_dict)


def list_of_prime_digits1(*args):
    sp = []
    for digit in args:
        if isprime(digit):
            sp.append(digit)
    return sp


def list_of_prime_digits2(*args):
    sp = []
    for digit in args:
        if isitprime(digit):
            sp.append(digit)
    return sp


print(list_of_prime_digits1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(list_of_prime_digits2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def uniqe_chars(string):
    set_of_char = set()
    for char in string:
        set_of_char.add(char)
    return list(set_of_char)


print(uniqe_chars('abcdefabccccddddeeeeffffz'))
