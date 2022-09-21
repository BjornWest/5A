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

for x in range(100):
    print(flippBlipp(x))