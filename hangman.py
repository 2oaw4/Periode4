def display_hangman(pogingen):
  stages = [  
              """
                 --------
                 |      |
                 |      O
                 |     \\|/
                 |      |
                 |     / \\
                 -
              """,

              """
                 --------
                 |      |
                 |      O
                 |     \\|/
                 |      |
                 |     /
                 -
              """,

              """
                 --------
                 |      |
                 |      O
                 |     \\|/
                 |      |
                 |
                 -
              """,

              """
                 --------
                 |      |
                 |      O
                 |     \\|
                 |      |
                 |
                 -
              """,

              """
                 --------
                 |      |
                 |      O
                 |      |
                 |      |
                 |
                 -
              """,

              """
                 --------
                 |      |
                 |      O
                 |
                 |
                 |
                 -
              """,

              """
                 --------
                 |      |
                 |
                 |
                 |
                 |
                 -
              """
  ]
 return stages[pogingen]


def main():
    woord = pak_woord()
    speel(woord)
    while input("Nog een keer? (J/N) ").upper() == "J":
        woord = pak_woord()
        speel(woord)

if __name__ == "__main__":
    main()


