import willekeurig
from woord import woord_lijst

def pak_woord():
  woord = willekeurig.keus(woord_lijst)
return wooord.upper() 


def speel(woord):
  woord_compleet = "_" * len(woord)
  geraden = False
  geraden_letters = []
  geraden_woorden = []
  pogingen = 6
  print("Laten we hangman spelen!")
  print(display_hangman(pogingen))
  print(woord_compleet)
  print("\n")
  while not geraden and pogingen > 0:
      raad = input("Raad een letter of een woord: ").upper()
      if len(raad) == 1 and raad.isalpha():
          if raad in geraden_letters:
              print("Je hebt deze letter al geraden", raad)
          elif raad not in woord:
              print(raad, "is niet in het woord.")
              pogingen -= 1
              geraden_letters.append(raad)
          else:
              print("Goed geraden,", raad, "is in het woord!")
              geraden_letters.append(raad)
              woord_as_list = list(woord_compleet)
              indices = [i for i, letter in enumerate(woord) if letter == raad]
              for index in indices:
                  woord_as_list[index] = raad
              woord_compleet = "".join(woord_as_list)
              if "_" not in woord_compleet:
                  geraden = True
                  print(woord_compleet)
                  print("Gefeliciteerd, je hebt het woord geraden!")
                  print("Je hebt", pogingen, "pogingen over.")
                  break
                  print(woord_compleet)
                  print("\n")
                  print(display_hangman(pogingen))
                  print("\n")
                  print("Je hebt", pogingen, "pogingen over.")
                  print("Geraden letters:", " ".join(geraden_letters))
                  print("Geraden woorden:", " ".join(geraden_woorden))
                  print("\n")
                  if pogingen == 0:
                      print("Je hebt geen pogingen meer over, het spel is afgelopen.")
                      print("Het woord was:", woord)
                      break
                      return geraden





   





















  