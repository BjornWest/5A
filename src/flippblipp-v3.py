def flippBlipp(n):
    out =  ""
    if n % 3 == 0:
        out+="flipp"
    if n % 5 == 0:
        if out != "":
            out+=" "
        out+="blipp"
    if out != "":
        return out
    else:
        return str(n)

x=0
while(True):
    x+=1
    if input("Nästa: ") != flippBlipp(x):
        print("Fel -",flippBlipp(x))
        print()
        print("Game Over")
        break