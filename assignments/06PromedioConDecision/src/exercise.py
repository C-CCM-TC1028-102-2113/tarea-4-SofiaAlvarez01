def main():
    #escribe tu código abajo de esta línea
    a= 0
    b=0
    n=1
    while n>0:
        n= float(input())
        if n>0:
            a= a+n
            b=b+1
    p= a/b
    print (p)  
    pass
if __name__=='__main__':
    main()
