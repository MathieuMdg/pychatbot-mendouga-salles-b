import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
def print_list(files_names):
    print(files_names)

def extraction(nom_fichier:list):
    extraction = []
    for i in nom_fichier:
        if i[-5] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            extraction.append((i[11:-5]))
        else:
            extraction.append((i[11:-4]))
    return extraction

def sans_doublon(liste:list):
    sans_doublon = []
    for i in liste:
        if i not in sans_doublon:
            sans_doublon.append(i)
    return sans_doublon

def prenom_nom(liste: list):
    prenom = {"Macron": "Emmanuel", "Mitterrand": "François", "Sarkozy": "Nicolas", "Giscard dEstaing": "Valéry", "Chirac": "Jacques", "Hollande": "François"}
    prenom_nom = []
    for i in liste:
        prenom_nom.append(prenom[i] + ' ' + i)
    return prenom_nom

def prenom_nom2(nom:str):
    prenom = {"Macron": "Emmanuel", "Mitterrand": "François", "Sarkozy": "Nicolas", "Giscard dEstaing": "Valéry", "Chirac": "Jacques", "Hollande": "François"}
    prenom_nom = ""
    prenom_nom = prenom[nom]
    return prenom_nom


directory = "./speeches"
files_names = list_of_files(directory, "txt")
print_list(files_names)


print(sans_doublon(extraction(files_names)))

prenom_president = {"Macron" : "Emmanuel", "Mitterrand" : "François", "Sarkozy" : "Nicolas", "Giscard dEstaing" : "Valéry", "Chirac" : "Jacques", "Hollande" : "François"}
print(prenom_president["Macron"])
print(sans_doublon(extraction(files_names)))

for i in files_names:
    fichier1 = open("./speeches/" + i, 'r')
    fichier2 = open("./speeches/hello.txt", 'w')
    contenu = fichier1.read()
    print(contenu)
    difference = int('a') - 65
    for elt in contenu:
        if (elt < 'Z') and (elt > "A"):
            elt = elt + (difference)
            print(elt)
        fichier2.write(elt)
