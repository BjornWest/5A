n = 100
def flippBlipp(n):
    
    for x in range(1,n):
        out =  ""
        if x % 3 == 0:
            out+="flipp"
        if x % 5 == 0:
            if out != "":
                out+=" "
            out+="blipp"
        if out != "":
            print(out)
        else:
            print(x)
flippBlipp(n)
