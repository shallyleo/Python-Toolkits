stringInp = str(input("Input a word: "))
print("Your input is : " + stringInp)

reversedString = ""
i = len(stringInp)
while i >= 1:
    reversedString+=(stringInp[i-1])
    i -=1
print("The reverse is: " + reversedString.lower())