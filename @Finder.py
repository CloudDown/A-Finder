import os
import webbrowser
from termcolor import colored


def checker_email():
    from pyisemail import is_email
    print(" ")
    address = str(input(colored("mets l'email que tu veux vérifier : ",'yellow')))
    bool_result_with_dns = is_email(address, check_dns=True)
    detailed_result_with_dns = is_email(address, check_dns=True, diagnose=True)

def main():
    Prenom = input(colored("Prenom : ",'yellow'))
    print(" ")

    nom = input(colored("Nom : ",'yellow'))
    print(" ")

    domain = input(colored("Domain (ex: @gmail.com) : ",'yellow'))
    print(" ")
    print(" ")

    print(colored(" Email exemple :",'green'))
    print(" ")

# .

    print(" - "+(Prenom)+"."+(nom)+""+(domain)+"")
    print(" - "+(Prenom)+""+(nom)+""+(domain)+"")
    print(" - "+(Prenom[0])+""+(nom)+""+(domain)+"")
    print(" - "+(nom)+""+(Prenom[0])+""+(domain)+"")
    print(" - "+(Prenom)+""+(domain)+"")
    print(" - "+(nom)+""+(domain)+"")
    print(" - "+(Prenom[0])+"."+(nom)+""+(domain)+"")
    print(" - "+(Prenom)+""+(nom[0])+""+(domain)+"")
    print(" - "+(Prenom)+"."+(nom[0])+""+(domain)+"")
    print(" - "+(Prenom[0])+""+(nom[0])+""+(domain)+"")
    print(" - "+(Prenom[0])+"."+(nom[0])+""+(domain)+"")
    print(" - "+(nom)+""+(Prenom)+""+(domain)+"")
    print(" - "+(nom)+"."+(Prenom)+""+(domain)+"")
    print(" - "+(nom)+"."+(Prenom[0])+""+(domain)+"")
    print(" - "+(nom[0])+""+(Prenom)+""+(domain)+"")
    print(" - "+(nom[0])+"."+(Prenom)+""+(domain)+"")
    print(" - "+(nom[0])+""+(Prenom[0])+""+(domain)+"")
    print(" - "+(nom[0])+"."+(Prenom[0])+""+(domain)+"")

# -

    print(" - "+(Prenom)+"-"+(nom)+""+(domain)+"")
    print(" - "+(Prenom[0])+"-"+(nom)+""+(domain)+"")
    print(" - "+(Prenom)+"-"+(nom[0])+""+(domain)+"")
    print(" - "+(Prenom[0])+"-"+(nom[0])+""+(domain)+"")
    print(" - "+(nom)+"-"+(Prenom)+""+(domain)+"")
    print(" - "+(nom)+"-"+(Prenom[0])+""+(domain)+"")
    print(" - "+(nom[0])+"-"+(Prenom)+""+(domain)+"")
    print(" - "+(nom[0])+"-"+(Prenom[0])+""+(domain)+"")

# _
    
    print(" - "+(Prenom)+"_"+(nom)+""+(domain)+"")
    print(" - "+(Prenom[0])+"_"+(nom)+""+(domain)+"")
    print(" - "+(Prenom)+"_"+(nom[0])+""+(domain)+"")
    print(" - "+(Prenom[0])+"_"+(nom[0])+""+(domain)+"")
    print(" - "+(nom)+"_"+(Prenom)+""+(domain)+"")
    print(" - "+(nom)+"_"+(Prenom[0])+""+(domain)+"")
    print(" - "+(nom[0])+"_"+(Prenom)+""+(domain)+"")
    print(" - "+(nom[0])+"_"+(Prenom[0])+""+(domain)+"")
    checker_email()






if __name__ == '__main__':
    os.system( "title Moony" )
    print(colored('''
                                          ______ _           _           
                           ____            |  ___(_)         | |          
                          / __ \   ______  | |_   _ _ __   __| | ___ _ __ 
                         / / _` | |______| |  _| | | '_ \ / _` |/ _ \ '__|
                        | | (_| |          | |   | | | | | (_| |  __/ |   
                         \ \__,_|          \_|   |_|_| |_|\__,_|\___|_|   
                          \____/                                             Program By CloudDown

''','cyan'))
    print(" ")
    print(colored('WRITE HELP FOR SHOW ALL COMMANDS', 'white', attrs=['bold']))
    print(" ")
    main()