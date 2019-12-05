# -*- coding: utf-8 -*-
def greet(name):
    print("hello "+name)

def run(number):
    if number>=0 and number<=10:
        for x in range(0,number):
            print("Running")
        print("--")
    else:
        print(number, "no está entre el 0 y el 10")



if __name__ == '__main__':
    greet("Hansel")
    greet("Grettel")
    run(5)
    run(8)
    run(12)
    run(9)
    run(15)
