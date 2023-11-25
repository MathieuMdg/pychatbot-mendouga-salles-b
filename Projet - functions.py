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
            ligne = suite_mot(ligne)
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


# Affiche le contenu d'un fichier donné dans un répertoire donné
def lecture(directory, file):
    lecture = ""
    for filename in os.listdir(directory):
        if file in filename:
            f = open(directory + "/" + file, 'r')
            contenu = f.readlines()
            for line in contenu:
                lecture = lecture + line
    return lecture


# Retourne une liste contenant tous les mots d'un texte
def liste_mot(texte:str):
    L = []
    mot = ""
    for lettre in texte:
        if lettre != " ":
            mot = mot + lettre
        else:
            L.append(mot)
            mot = ""
    return L






#Calcul le TF d'une chaine de caractère
def TF(texte: str):
    TF = {}
    texte_mots = liste_mot(texte)
    for elt in texte_mots:
        if elt in TF:
            TF[elt] = TF[elt] + 1
        else:
            TF[elt] = 1
    return TF


directory = "./speeches"
files_names = list_of_files(directory, "txt")
print_list(files_names)
minuscule(directory, "txt") # Appel de la fonction minuscule pour créer et remplir le fichier cleaned


# Pas encore terminé
def IDF(directory):
    dico = {}
    Liste_files = list_of_files(directory, "txt") #Créer une liste du nom de chaque fichier du dossier
    Liste_mot = []
    nbre_fichier = len(Liste_files)
    for elt in Liste_files:
        Liste_mot = Liste_mot + liste_mot(lecture(directory, elt)) #puis la fonction lecture pour lire le contenu du fichier et enfin la fonction liste de mot pour créer une liste des mots du fichier.
    Liste_mot = sans_doublon(Liste_mot)
    for mot in Liste_mot:
        nbre_fichier_mot = 0
        for i in Liste_files:
            L = []
            L = liste_mot(lecture(directory, i))
            if mot in L:
                nbre_fichier_mot += 1
            if nbre_fichier_mot == 0:
                dico[mot] = "pas de mot"
            else:
                IDF = math.log((nbre_fichier / nbre_fichier_mot) + 1)
                dico[mot] = IDF
    return dico


# Effectue le dictionnaire TF de chaque document
files_cleaned = list_of_files("./cleaned", "txt")
dictionnaire_files = {}
for files in files_cleaned:
    print("Le nombre TF du fichier", files, "est :")
    print(TF(lecture("./cleaned", files)))
    print("")
    dictionnaire_files[files] = TF(lecture("./cleaned", files))
    print(dictionnaire_files)

IDF = IDF("./cleaned")
for i in range(10):
    x = str(input("Saisir un mot : "))
    print(IDF[x])


#_______________________________________________________________________________________________________________________________________________________|

def TF(chaine:str):

    assert isinstance(chaine, str)
    chaine = chaine + " "
    dico = {}
    mot = ""
    for lettres in chaine: 
        
        if lettres == " ":
            
            if mot in dico:
                dico[mot] = dico[mot] + 1
                mot = ""
                
            else:
                dico[mot] = 1
                mot=""
            
        else:
            mot = mot + lettres
    return dico

#--------------------------------------------|

def IDF():
    arr = os.listdir("speeches")
    txtfiles = []
    
    for file in arr:
        print(file)
        f = open(f"speeches\{file}", "r+", encoding = "utf-8")
        
        for x in f:
            print(TF(str(f.readline())))
            txtfiles.append(file)
        #print(TF(str(f.readline())))
        #txtfiles.append(file)
    print(txtfiles)
    return 0

#____________________________________________________________________________________________________|
#--------------------------------------------|

def extraction():
    arr = os.listdir("speeches")

    liste_nomP = []
    
    for file in arr:
        decod = False
        stock = ""
        print(file)
        for x in range(len(file)-4):

            if decod == True and ord(str.lower(file[x])) >= 97 and ord(str.lower(file[x])) <= 122:
                stock += file[x]

            if file[x] == "_":
                decod = True
                
        if stock not in liste_nomP:
            liste_nomP.append(stock)

    return liste_nomP

#--------------------------------------------|
prenomP = {"Chirac": "Jacques", "Giscard dEstaing": "Valéry", "Hollande": "François", "Macron": "Emmanuel", "Mitterrand": "François", "Sarkozy": "Nicolas"}

def associa(listeP):
    pren = []
    for x in listeP:
        pren.append(prenomP[x])
    
    return pren

#--------------------------------------------|

def conversMin():
    arr = os.listdir("speeches")
    
    for file in arr:

        f = open(f"speeches\{file}", "r+", encoding = "utf-8")
        g = open(f"cleaned\{file}", "w", encoding = "utf-8")
        for x in f:
    
            g.write(str(str.lower(x)))
    f.close()
    g.close()
    return None

#--------------------------------------------|
listPonc = ["'", "-", "_", ",", "?", "!", ".", ";", ":", "/", "(", ")"]

def triPonc():
    
    brr = os.listdir("cleaned")
    
    for file in brr:

        f_init = open(f"cleaned\{file}", "r", encoding = "utf-8")     
        lecture = f_init.readlines()
        f_init.close()
        
        for x in lecture:
            fall = ""
            for y in x:
                
                if y in listPonc:
                    fall += " "
                else:
                    fall += y
            print(fall)
            f_trs = open(f"cleaned\{file}", "w", encoding = "utf-8")
            f_trs.write(fall)
            f_trs.close() 


    return None
