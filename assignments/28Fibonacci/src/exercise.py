
def main():
    #escribe tu código abajo de esta línea
    c=1
    a=0
    b=1
    num= int(input("Enter the index: "))
    if num==0:
        print (0)
    if num==1:
        print (1)     
    while c<num:
        c=c+1 
        d=a+b
        if num==c:
            print (d)
        a=b
        b=d
    pass

if __name__=='__main__':
    main()
