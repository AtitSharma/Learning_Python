def RemoveA(String):
    if String=="":
        return ""
    if String.startswith("apple"):
        return RemoveA(String[5:])
    else:
        return  String[0] +RemoveA(String[1:])
print(RemoveA("aaappleaaabracadabrapplea"))
