#Para este código se debe presionar el botón "Run"
print("Te doy la bienvenida")
import random

options = ("piedra", "papel", "tijera") 

nombre = input("¿Cuál es tu nombre? ")

computer_wins = 0
print(computer_wins)
user_wins = 0
print(user_wins)

rounds = 1

while True:
  
    print("*" * 10)
    print("ROUND", rounds)
    print("*" * 10)
  
    computer_option = random.choice(options)
    user_option = input("Elije entre piedra, papel, o tijera: ") 
    user_option = user_option.lower()
  
    if not user_option in options:
        print("Elegiste una opción no válida, intenta de nuevo...")

    print(f"Opción de {nombre}: ", user_option)
    print("Opción de la computadora: ", computer_option)
  
    if user_option == computer_option:
      print(" ¡¡Empate!! ")
    elif user_option == "piedra":
        if computer_option == "tijera":
          print("Piedra gana a tijera")
          print(f"¡¡{nombre} Ganaste!!")
          user_wins += 1
        else:
          print("Papel gana al piedra") 
          print("la computadora ganó...")
          computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
          print("Papel le gana a piedra")
          print(f"¡¡{nombre} Ganaste!! ")
          user_wins += 1
        else:
          print("Tijera gana a papel") 
          print("La computadora ganó...")
          computer_wins += 1    
    elif user_option == "tijeras":
        if computer_option == "papel":
          print("Tijeras le gana a papel")
          print(f"¡¡{nombre} Ganaste!! ")
          user_wins += 1
        else:
          print("Piedra gana a tijera") 
          print("La computadora ganó...")
          computer_wins += 1
    if computer_wins == 2:
          print("La computadora gana la partida, buenas suerte la próxima")
          break
    if user_wins == 2:
          print("¡¡Le has ganado a la computadora, felicitaciones!!")
          break
    rounds += 1 