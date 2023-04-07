import os

def  subMenuGame():
    subControl = True

    while subControl:
        os.system("cls")

        subMenu = "Select Game to Play\n\nS - Short Game\nL - Long Game\n----------------------\nX - Back Previous Menu\n"

        print(subMenu)
        subSelect = input("Please, choose an option: ")

        match subSelect:
            case "S" | "s" : print("Selected Short Game")
            case "L" | "l" : print("Selected Long Game")
            case "X" | "x" : break
            case _: input("\nInvalid selection, please try again. (Press any key to continue)")