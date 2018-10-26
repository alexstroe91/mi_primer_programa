#Preguntamos al usuario que nos diga un numero, y si es el que nosotros estamos pensando le decimos que ha ganado y si no, que ha perdido, tiene 5 itentos.

#Definimos el numero en el que estamos pensando
number_to_guess = 2

#Le decimos al usuario que tiene 5 intentos:
print("Tienes solo 5 intentos, ¡piensa bien!")

#Le pedimos al usuario que nos diga un numero del 1 al 15
user_number = int(input("Dime un numero del 1 al 15: "))

#Definimos la condición.
if user_number == number_to_guess:
    print ("¡ Has ganado !")


#Si falla le decimos que le quedan 4 intentos más
else:
    print("Has fallado :( te quedan 4 intentos más")
    print("")
    user_number = int(input("Dime un numero del 1 al 15: "))
    if user_number == number_to_guess:
        print("¡Has ganado ! :)")
    else:
        print("Has fallado :( te quedan 3 intentos.")
        print("")
        user_number = int(input("Dime un numero del 1 al 15: "))
        if user_number == number_to_guess:
            print("¡Has ganado ! :)")
        else:
            print("Has fallado :( te quedan 2 intentos.")
            print("")
            user_number = int(input("Dime un numero del 1 al 15: "))
            if user_number == number_to_guess:
                print("¡Has ganado ! :)")
            else:
                print("Has fallado :( te quedan 1 intentos.")
                print("")
                user_number = int(input("Dime un numero del 1 al 15: "))
                if user_number == number_to_guess:
                    print("¡Has ganado ! :)")
                else:
                    print("Has perdido, ya no te quedan más intentos :( ")