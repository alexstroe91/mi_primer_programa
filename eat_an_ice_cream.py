
apetece_helado_input = input("Te apetece un helado ? (Si/No) : ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado= False
else:
    print("Te he dicho que me digas si on o, no se que has dicho pero cuento como que no ")
    apetece_helado = False

tiene_dinero_input = input("Tienes dinero para un helado ? (Si/No) : ").upper()
senor_helados_input = input("Esta el señor de los helados ? (Si/No) : ").upper()
esta_tu_tia_input = input("¿Estás con tu tía ? (Si/No) : ").upper()

tiene_dinero = tiene_dinero_input == "SI"
esta_tu_tia = esta_tu_tia_input == "SI"
puedes_permitirtelo = tiene_dinero == "SI" or esta_tu_tia_input == "SI"
senor_helados = senor_helados_input == "SI"



if apetece_helado and puedes_permitirtelo and senor_helados:
    print("Comprate un helado")

else:
    print("Pues no te lo comes")


