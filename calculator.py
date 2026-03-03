def calculator_choice():
    choice = None

    while choice not in ["1","2","3","4"]:
        print("Python Taschenrechner")
        print("1 = Addition")
        print("2 = Subtraktion")
        print("3 = Multiplikation")
        print("4 = Division")

        choice = input("Wähle eine Option:")
        print("Du hast gewählt:",choice)

        if choice not in ["1","2","3","4"]:
            print("Ungültige Option, bitte erneut wählen.")

    return choice


def calculator():
    choice = calculator_choice()

    match choice:
        case "1":
            print("Addition ausgewählt.")
            zahl1 = float(input("Erste Zahl:"))
            zahl2 = float(input("Zweite Zahl:"))
            ergebnis = zahl1 + zahl2
            print("Ergebnis",ergebnis)
        case "2":
            print("Subtraktion ausgewählt.")
            zahl1 = float(input("Erste Zahl:"))
            zahl2 = float(input("Zweite Zahl:"))
            ergebnis = zahl1 - zahl2
            print("Ergebnis",ergebnis)
        case "3":
            print("Multiplikation ausgewählt.")
            zahl1 = float(input("Erste Zahl:"))
            zahl2 = float(input("Zweite Zahl:"))
            ergebnis = zahl1 * zahl2
            print("Ergebnis",ergebnis)
        case "4":
            print("Division ausgewählt.")
            zahl1 = float(input("Erste Zahl:"))
            zahl2 = float(input("Zweite Zahl:"))

            if zahl2 == 0:
                print("Fehler: Division durch Null ist nicht erlaubt.")
                return

            ergebnis = zahl1 / zahl2

            print("Ergebnis",ergebnis)


while True:
    calculator()

    nochmal = input("Neue Rechnung starten? (y/n):")
    if nochmal =="n":
        break
