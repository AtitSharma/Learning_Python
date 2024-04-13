from itertools import permutations
# GLOBAL_ARR = []

def permutaions(string):
    if is_palindrome(string):
        return len(string)
    result =list(filter(is_palindrome,["".join(tuple(permutation)) for i in range(len(string)+1) for permutation in permutations(string, i)])) 
    # result.sort(key=len)
    return len(result[-1])
   
    

def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False

# print(GLOBAL_ARR)

# ans = list(filter(is_palindrome,GLOBAL_ARR))
# print(ans)

print(permutaions("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))
