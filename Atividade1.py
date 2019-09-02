
import string


def bit(num):
    if num % 2 > 0:
        return str(1)

    else:
        return str(0)


def toBin(num):
    if num > 1:
        return toBin(int(num/2)) + bit(num)
    else:
        return bit(num)


def up(num):
    if num <= 1000:
        print(num)
        return up(num * 2)
    else:
        return num / 2


def down(num, lim):
    if num >= lim:
        print(int(num))
        return down(num / 2, lim)
    else:
        return num


def sequence(num):
    down(up(num), num)


def p(num):
    return num - 1


def s(num):
    return num + 1


def soma(x, y):
    if y == 0:
        return x
    else:
        return soma(s(x) if y > 0 else p(x), p(y) if 0 < y else s(y))


def hiper(n):
    if n > 1:
        return hiper(n - 1) * (n ** n)
    else:
        return 1


def contains(a, b):
    if len(a) == 0:
        return True
    if a[0] in b:
        a = removeFirst(a)
        return contains(a, b)
    else:
        return False


def removeFirst(s):
    return list(filter(lambda x: x != s[0], s))


def replace(s, new, index):
    out = ''
    for x in range(0, len(s)):
        if x != index:
            out += s[x]
        else:
            out += new
    return out
    
def plusOneBit(num):
    for bit in range(len(num) - 1, 0, -1):
        if num[bit] == '0':
            num = replace(num, '1', bit)
            break
        else:
            num = replace(num, '0', bit)
    return num

def toDec(num):
    n = len(num) - 1
    out = 0
    for bit in num:
        out += int(bit) * (2 ** n)
        n = n - 1
    return out

def complementOf2(num):
    if num[0] == '1':
        out = ''
        for bit in num:
            out += '1' if bit == '0' else '0'
        out = plusOneBit(out)
        n = toDec(out)
        return (n if n != 0 else int((2 ** len(num)))) * -1
    else:
        return toDec(num)


print(complementOf2('1' + toBin(50)))
