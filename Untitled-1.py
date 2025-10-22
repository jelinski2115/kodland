import random

znaki = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

dlugosc = int(input("Ile ma mieć hasło znaków? "))

haslo = ""

for i in range(dlugosc):
    haslo = haslo + random.choice(znaki)

print("Twoje hasło to:", haslo)
