def main():
    #escribe tu código abajo de esta línea
    n= int(input("ingresa un numero"))
    a=0
    c= "#"
    d=1
    while a<n:
        print (d,"-",c)
        if c== "#":
            c= "%"
        elif c== "%":
            c= "#"
        a=a+1
        d=d+1
    pass

if __name__=='__main__':   
    main()
