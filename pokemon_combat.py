
user_pokemon = print("¡ Tienes un Pikachu, asi que vas a luchar con él !"
                     " \n  El Pikachu tiene 100 de vida y 2 ataques, Bola voltio y Rayo"
                     "\n  Bola voltio hace 12 de daño y Rayo hace 10 de daño.")

enemy_pokemon = input("¿Contra qué pokemon quieres combatir? (Squirtle / Charmander / Bulbasur) ").upper()

pikachu_life = 100
enemy_life = 0

if enemy_pokemon == "SQUIRTLE":
     enemy_life = 90
     print("Vas a luchar contra Squirtle")
     pokemon_name = "SQUIRTLE"
     pokemon_atack = 8

elif enemy_pokemon == "CHARMANDER":
     enemy_life = 80
     print("Vas a luchar contra Charmander")
     pokemon_name = "CHARMANDER"
     pokemon_atack = 7

elif enemy_pokemon == "BULBASUR":
     enemy_life = 100
     print("Vas a luchar contra Bulbasur")
     pokemon_name = "BULBASUR"
     pokemon_atack = 10


pikachu_life = 100

while pikachu_life > 0 and enemy_life > 0:
    ataque_elegido = input("¿Qué ataque quieres utilizar? (Rayo / Bola voltio) ").upper()
    if ataque_elegido == "RAYO":
         enemy_life -= 10
         print("Pikachu ha usado Bola Voltio. Vida de {} -10 PV \n Los PV de {} ahora son {} ".format(str(pokemon_name), str(pokemon_name), int(enemy_life)))
    if ataque_elegido == "BOLA VOLTIO":
         enemy_life -= 12
         print ("Pikachu ha usado Bola Voltio. Vida de {} -12 PV \n Los PV de {} ahora son {}".format (str(pokemon_name), str(pokemon_name), int(enemy_life)))


    if enemy_pokemon == str(pokemon_name):
         pikachu_life -= int(pokemon_atack)
         print("{} ha usado un ataque básico. Vida de Pikachu -{} PV. \n La vida de Pikachu ahora es {}" .format (str(pokemon_name), int(pokemon_atack), int(pikachu_life)))


if enemy_life <= 0:
    print("¡Has ganado el combate!")
elif pikachu_life <= 0:
    print("Has perdido el combate")
print("")
print("")


print("El combate ha termiando")