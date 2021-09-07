
def main():
    #Escribe tu código debajo de esta línea
    h= int(input("Enter triangle height: "))
    a=0
    b=0
    while a<h:
        a=a+1
        b=h-a
        print (" "*b,"*"*a)
    pass


if __name__=='__main__':
    main()
