import os


# Créer une liste avec le nom de tous les fichiers
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


directory = "./speeches"
files_names = list_of_files(directory, "txt")
print_list(files_names)
