#!/data/data/com.termux/files/usr/bin/python3

print("Te damos la bienvenida a Habilcom")

name = input("Ingresa tu nombre: ")

print(f"Hola, {name}")

age = int(input("Cual es tu edad? "))

if age >= 18:
    print("Puedes usar este sitio")
else:
    print("No puedes usar este sitio")