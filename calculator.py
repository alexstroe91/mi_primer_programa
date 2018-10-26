
operacion_a_realizar = input("¿Qué operación quieres realizar? ( sumar / restar / multiplicar / dividir ): ").upper()

primer_sumando = int(input("Primer sumando: "))
segundo_sumando = int(input("Segundo sumando: "))

if operacion_a_realizar == ("SUMAR"):
    resultado = primer_sumando + segundo_sumando
    print("El resultado de la suma es: " + str(resultado))
elif operacion_a_realizar == ("RESTAR"):
    resultado = primer_sumando - segundo_sumando
    print("El resultado de la resta es: " + str(resultado))
elif operacion_a_realizar == ("MULTIPLICAR"):
    resultado = primer_sumando * segundo_sumando
    print("El resultado de la multiplicación es: " + str(resultado))
elif operacion_a_realizar == ("DIVIDIR"):
    resultado = primer_sumando / segundo_sumando
    print("El resultado de la división es: " + str(resultado))


