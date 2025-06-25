import random
# levens
GALGJE_PLAATJES = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\\  |
 / \\  |
     ===''']

# Woordenlijst 
WOORDENLIJST = ['python', 'galgje', 'uitdaging', 'programmeren', 'tovenaar', 'toverij', 'toetsenbord']

# Kies een random woord uit de lijst
def kies_willekeurig_woord():
    return random.choice(WOORDENLIJST).upper()

# Toon de status van het spel
def toon_spel(galg_plaatjes, foute_letters, juiste_letters, geheime_woord):
    print(galg_plaatjes[len(foute_letters)])
    print()

    print("Foute letters:", ' '.join(foute_letters))

    lege_vakken = ['_' if letter not in juiste_letters else letter for letter in geheime_woord]
    print(' '.join(lege_vakken))
    print()

# Vraag om een letter van de gebruiker
def vraag_letter(al_geraden):
    while True:
        gok = input("Raad een letter: ").upper()
        if len(gok) != 1:
            print("Voer slechts één letter in.")
        elif not gok.isalpha():
            print("Voer een LETTER in.")
        elif gok in al_geraden:
            print("Je hebt die letter al geraden.")
        else:
            return gok

# Vraag of de speler opnieuw wil spelen
def opnieuw_spelen():
    return input("Wil je opnieuw spelen? (ja of nee): ").lower().startswith('j')

# repeat van het spel
def speel_galgje():
    print("G A L G J E")
    foute_letters = []
    juiste_letters = []
    geheime_woord = kies_willekeurig_woord()
    spel_klaar = False

    while True:
        toon_spel(GALGJE_PLAATJES, foute_letters, juiste_letters, geheime_woord)

        gok = vraag_letter(foute_letters + juiste_letters)

        if gok in geheime_woord:
            juiste_letters.append(gok)

            alles_gevonden = all(letter in juiste_letters for letter in geheime_woord)
            if alles_gevonden:
                print(f"\nGoed gedaan! Het geheime woord was '{geheime_woord}'! Je hebt gewonnen!")
                spel_klaar = True
        else:
            foute_letters.append(gok)

            if len(foute_letters) == len(GALGJE_PLAATJES) - 1:
                toon_spel(GALGJE_PLAATJES, foute_letters, juiste_letters, geheime_woord)
                print(f"\nJe hebt geen pogingen meer over!\nHet woord was '{geheime_woord}'.")
                spel_klaar = True

        if spel_klaar:
            if opnieuw_spelen():
                foute_letters = []
                juiste_letters = []
                geheime_woord = kies_willekeurig_woord()
                spel_klaar = False
            else:
                break

# Start van spel
if __name__ == "__main__":
    speel_galgje()
