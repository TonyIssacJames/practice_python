from fractions import Fraction


def product(fracs):
    for t in fracs:
        print(t)
    return 0



if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))

    result = product(fracs)
    print(result)


