
user_pokemon = print("¡ Tienes un Pikachu, asi que vas a luchar con él !"
                     " \n  El Pikachu tiene 100 de vida y 2 ataques, Bola voltio y Rayo"
                     "\n  Bola voltio hace 12 de daño y Rayo hace 10 de daño.")

enemy_pokemon = input("¿Contra qué pokemon quieres combatir? (Squirtle / Charmander / Bulbasur) ").upper()

pikachu_life = 100
enemy_life = 0

if enemy_pokemon == "SQUIRTLE":
    enemy_life = 90
    print("Vas a luchar contra Squirtle")
if enemy_pokemon == "CHARMANDER":
    enemy_life = 80
    print("Vas a luchar contra Charmander")
if enemy_pokemon == "BULBASUR":
    enemy_life = 100
    print("Vas a luchar contra Bulbasur")

pikachu_life = 100

while pikachu_life > 0 and enemy_life > 0:
    ataque_elegido = input("¿Qué ataque quieres utilizar? (Rayo / Bola voltio) ").upper()
    if ataque_elegido == "RAYO":
         enemy_life -= 10
         print("Pikachu ha usado Rayo. Vida de " + enemy_pokemon + " -10 \n " + "La vida de " + enemy_pokemon + " ahora es " + str(enemy_life))


    if ataque_elegido == "BOLA VOLTIO":
         enemy_life -= 12
         print("Pikachu ha usado Bola Voltio. Vida de " + enemy_pokemon + " -12 \n " + "La vida de " + enemy_pokemon + " ahora es " + str(enemy_life))

    if enemy_pokemon == "SQUIRTLE":
         pikachu_life -= 8
         print("Squirtle ha usado un ataque básico. Vida de Pikachu -8. \n La vida de Pikachu ahora es " + str(pikachu_life))
    if enemy_pokemon == "CHARMANDER":
         pikachu_life -= 7
         print("Charmander ha usado un ataque básico. Vida de Pikachu -8. \n La vida de Pikachu ahora es " + str(pikachu_life))
    if enemy_pokemon == "BULBASUR":
         pikachu_life -= 10
         print("Bulbasur ha usado un ataque básico. Vida de Pikachu -8. \n  La vida de Pikachu ahora es " + str(pikachu_life))


if enemy_life <= 0:
    print("¡Has ganado el combate!")
if pikachu_life <= 0:
    print("Has perdido el combate")
print("")
print("")

print("El combate ha termiando")