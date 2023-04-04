import os

os.system("cls")

mainMenu = "Main Menu\n\nP - Play Game\nR - Replay Game\nE - Enter Previous Data\nV - View Data\nD - Delete Data\n-----------------------\nX - Exit"

print(mainMenu)
mainSelect = input("Please, choose an option: ")

match mainSelect:
    case "P" | "p" : print("You choose play a game.")
    case "R" | "r" : print("You choose replay a game.")
    case "E" | "e" : print("You choose enter previous data.")
    case "V" | "v" : print("You choose view data of the database.")
    case "D" | "d" : print("You choose delete data of the database.")
    case "X" | "x" : print("You choose exit the game.")
    case _: input("\nInvalid selection, please try again. (Press any key to continue)")