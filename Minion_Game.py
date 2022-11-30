def minion_game(s):
    ks = ss = 0
    for i in range(len(s)):
        if s[i] in "AEIOU":
            ks += len(s) - i
        else:
            ss += len(s) - i

    if ks > ss:
        print("Kevin", ks)
    elif ss > ks:
        print("Stuart", ss)
    else:
        print("Draw")


if __name__ == "__main__":
    s = input()
    minion_game(s)