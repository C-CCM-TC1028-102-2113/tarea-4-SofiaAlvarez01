def main():
    #escribe tu código abajo de esta línea
    n= int(input())
    a=0
    c= "#"
    while a<n:
        print (c)
        if c== "#":
            c= "%"
        elif c== "%":
            c= "#"
        a=a+1
    pass

if __name__=='__main__':   
    main()
