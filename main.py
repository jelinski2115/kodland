print("Witam w moim słowniku memów!")
print("Wpisuj słowa wielkimi literami.")
print("Jeśli nie znasz słowa, możesz dodać 5 nowych słów do słownika naraz.")

meme_dict = {
    "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
    "LOL": "Częsta reakcja na coś zabawnego",
    "ROFL": "Odpowiedź na żart",
    "SHEESH": "Lekka dezaprobata",
    "CREEPY": "Straszny, złowieszczy",
    "AGGRO": "Stać się agresywnym/zły"
}

while True:
    word = input("\nWpisz słowo (lub EXIT, aby zakończyć): ").strip().upper()

    if word == "EXIT":
        print("Do zobaczenia!")
        break

    if word in meme_dict:
        print("{} — {}".format(word, meme_dict[word]))
    else:
        print("Nie znam tego słowa. Dodaj więcej słów do słownika!")
        print("Dodaj 5 nowych słów:")
        for i in range(5):
            new_word = input("Podaj nowe słowo nr {} (wielkimi literami): ".format(i+1)).strip().upper()
            new_def = input("Podaj definicję dla '{}': ".format(new_word)).strip()
            meme_dict[new_word] = new_def
        print("Dodałem 5 nowych słów do słownika! Spróbuj teraz ponownie.")
