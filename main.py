




count = 1
n = int(input('Введите число: '))

def Exponentiation (count, n):

    while count <= n:
        print(count ** 3)
        count += 1

if __name__ == '__main__':
    Exponentiation(count, n)