
mi_lista  = []
input_usuario = ""

while  input_usuario != "FIN":
    input_usuario = input("¿Qué necesitas comprar? (Escribe FIN para terminar): ")
    if input_usuario != "FIN":
        mi_lista.append(input_usuario)

largo_lista = len(mi_lista)
indice_acutal = 0


for item in mi_lista :
    print ("Tengo que comprar {}".format(item))

print("Es la lista de la compra")
if len(mi_lista) == 0 :
    print("No hay que comprar nada")