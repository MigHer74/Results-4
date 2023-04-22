import os
import launcher as lnr
import dbactions as dba

dba.verify_tbl()

mainControl = True

while mainControl:
    os.system("cls")

    mainMenu = "Main Menu\n\nP - Play Game\nR - Replay Game\nE - Enter Previous Data\nV - View Data\nD - Delete Data\n-----------------------\nX - Exit\n"

    print(mainMenu)
    mainSelect = input("Please, choose an option: ")

    match mainSelect:
        case "P" | "p" : lnr.subMenuGame()
        case "R" | "r" : print("You choose replay a game.")
        case "E" | "e" : print("You choose enter previous data.")
        case "V" | "v" : print("You choose view data of the database.")
        case "D" | "d" : print("You choose delete data of the database.")
        case "X" | "x" : break
        case _: input("\nInvalid selection, please try again. (Press any key to continue)")
