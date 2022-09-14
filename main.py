chaine = str(input("Entrer votre phrase: "))
chaine = chaine.lower()
chaine = chaine.replace("'", " ")

def count_word():

    return len(chaine.split(" "))

nombre_mot = count_word()
print(nombre_mot)