import os
import shutil
import math

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

# Affiche la liste
def print_list(files_names):
    print(files_names)


# Extrait les noms de fichier de la liste et ajoute les noms des présidents dans une nouvelle liste
def extraction(nom_fichier: list):
    L = []
    for i in nom_fichier:
        if i[-5] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            L.append((i[11:-5]))
        else:
            L.append((i[11:-4]))
    return L


# Permet de supprimer les doublons d'une liste
def sans_doublon(liste: list):
    L = []
    for i in liste:
        if i not in L:
            L.append(i)
    return L


# Associe à chaque noms de président un prénom et l'ajoute dans une liste
def prenom_nom(liste: list):
    prenom = {"Macron": "Emmanuel", "Mitterrand": "François", "Sarkozy": "Nicolas", "Giscard dEstaing": "Valéry",
              "Chirac": "Jacques", "Hollande": "François"}
    L = []
    for i in liste:
        L.append(prenom[i] + ' ' + i)
    return L


# Créer un fichier avec les textes en minuscule
def minuscule(directory, extension):
    files_names = []
    os.mkdir("cleaned")
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    for fichier in files_names:
        f = open(directory + "/" + fichier, "r")
        contenu = f.readlines()
        for ligne in contenu:
            ligne = ligne.lower()
            print(ligne)
            f2 = open("./cleaned" + "/" + fichier.lower(), "a")
            f2.write(ligne)
        f2.close()
    f.close()


# Supprime tous les ',?! etc des textes d'un fichier
def suite_mot(texte:str):
    characters = "!?.,;()[]_'-"
    for x in range(len(characters)):
        if characters[x] in characters[:-3]:
            texte = texte.replace(characters[x], "")
        else:
            texte = texte.replace(characters[x], " ")
            texte = texte.replace('\n', " ")
    return texte




directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(minuscule(directory, "txt"))

for filename in os.listdir("./cleaned2"):
    f = open("./cleaned2" + "/" + filename, "r")
    TF = {}
    Liste = []
    contenu = f.readlines()
    for ligne in contenu:
        TF = {}
        Liste = ligne.split(" ")
        for elt in Liste:
            if elt in TF:
                TF[elt] = TF[elt] + 1
            else:
                TF[elt] = 1
        print(Liste)
        print(TF)


#Calcul le TF d'une chaine de caractère
def TF(texte: str):
    TF = {}
    texte_mots = texte.split(" ")
    for elt in texte_mots:
        if elt in TF:
            TF[elt] = TF[elt] + 1
        else:
            TF[elt] = 1
    return TF


directory = "./speeches"
files_names = list_of_files(directory, "txt")
print_list(files_names)
minuscule(directory, "txt")

for i in range(len(files_names):
    f = open(files_names[i], 'r')

def IDF(direcory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)