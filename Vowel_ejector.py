def vowel_ejector(String):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result=''
    for i in String:
        if i not in vowel :
            result+=i
    return result
String=input("Enter String : ")
print(vowel_ejector(String))
