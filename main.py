from sys import *
from os import *
from filecmp import *
import shutil
 
def verif():
    if len(argv)<=3:
        exit("Utilisation : ce programme necessite au moins 3\
        arguments : le repertoire source, le repertoire cible et le\
        mode de synchronisation (ex force pour copier l'integalite\
        des fichiers de sources vers cible)" )
 
#comparer le contennu des fichier
def force(source, cible):
 
    list=dircmp(source,cible)
    list.report()
    for i in list.left_list:
        print (i)

#copier les fichiers de source vers cible    
def copier (source,cible):
    filePath = shutil.copy(source,cible)
    print("le répertoire source est coppier dans: "+filePath)    
    #cela affiche /home/user/doc/file.txt
 
# Debut prog principal
 
verif()  #verif nbre parametres
 
#verification de l'existence des repertoires
 
if access(argv[1],F_OK)==0:
    print ("Le dossier source n'existe pas, verifier et recommencer")
 
if access(argv[2],F_OK)==0:
    while 1:
        rep=input("Le dossier cible n'existe pas, voulez vous le creer o/n ?" )
        if rep=="n":
            exit("Abandon utilisateur" )
        if rep=="o":
            mkdir(argv[2])
            break
     
if argv[3]=="force":
    force(argv[1],argv[2])

if argv[3]=="copier":
    copier(argv[1],argv[2])