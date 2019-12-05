
def greet(name):
    print("hello "+name)

def run(number):
    if number>=0 and number<=10:
        for x in range(0,number):
            print("Running")
    else:
        print(number, "no esta entre el 0 y el 10")




friend=str(input("Escribe tu nombre: "))
greet(friend)

num=int(input("Escriba un numero de 0 a 10: "))
run(num)