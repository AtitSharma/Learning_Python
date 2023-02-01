def RemoveA(String):
    if String=="":
        return ""
    char=String[0]
    if char=="a":
        return RemoveA(String[1:])
    else:
        return  char +RemoveA(String[1:])
print(RemoveA("aaaaaabracadabra"))
