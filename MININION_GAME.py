def minion_game(string):
    vowel=0
    conconent=0
    s=len(string)
    for i in range (s):
        if string[i] in 'AEIOU':
            vowel+=s-i
        else:
            conconent+=s-i
    if conconent>vowel:
        print("Stuart {}".format(conconent))
    elif conconent==vowel:
        print("Draw")
    else :
        print("Kevin {}".format(vowel))

if __name__ == '__main__':
    s = input()
    minion_game(s)