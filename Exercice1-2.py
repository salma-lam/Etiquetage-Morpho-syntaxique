# Importation de defaultdict pour la fonction apprendre_Etiquettes
from collections import defaultdict

################  Exercice 1  ################

# Fonction apprendre_Etiquettes qui apprend les étiquettes les plus fréquentes
def apprendre_Etiquettes(corpus):
    lexique = defaultdict(lambda: defaultdict(int))  # Dictionnaire temporaire pour compter les étiquettes
    for mot, etiquette in corpus:
        lexique[mot][etiquette] += 1  # Comptage des étiquettes par mot
    
    lexique_final = {}
    for mot, etiquettes in lexique.items():
        lexique_final[mot] = max(etiquettes, key=etiquettes.get)  # Sélection de l'étiquette la plus fréquente
    
    return lexique_final

# Fonction principale qui combine l'apprentissage des étiquettes
def Apprendre_lexique(corpus):
    lexique = apprendre_Etiquettes(corpus)  # Génération du lexique
    return lexique

# Corpus d'exemple à utiliser pour tester
corpus = [
    ('la', 'DET'), ('belle', 'ADJ'), ('femme', 'N'), 
    ('ferme', 'V'), ('la', 'DET'), ('porte', 'N'), 
    ('.', 'PONCT'), ('la', 'DET'), ('ferme', 'ADJ'),
]

# Appel de la fonction Apprendre_lexique pour tester
lexique = Apprendre_lexique(corpus)

# Affichage du lexique pour vérifier le résultat
print("Lexique généré :")
for mot, etiquette in lexique.items():
    print(f"Mot: {mot}, Étiquette: {etiquette}")


################  Exercice 2  ################

# Fonction pour réétiqueter un corpus en utilisant le lexique
def Retiqueter_corpus(corpus, lexique):
    nouveau_corpus = []
    for mot, etiquette in corpus:
        nouvelle_etiquette = lexique.get(mot, etiquette)  # Utilise l'étiquette du lexique si elle existe
        nouveau_corpus.append((mot, nouvelle_etiquette))
    return nouveau_corpus

# Fonction pour comparer deux corpus (corpus de référence et corpus réétiqueté)
def Comparer(corpus_reference, corpus_test):
    erreurs = 0
    for (mot_ref, etiquette_ref), (mot_test, etiquette_test) in zip(corpus_reference, corpus_test):
        if etiquette_ref != etiquette_test:  # Si les étiquettes diffèrent, on compte une erreur
            erreurs += 1
    return erreurs

# Corpus d'apprentissage étiqueté
corpus_apprentissage = [
    ('la', 'DET'), ('belle', 'ADJ'), ('femme', 'N'), 
    ('ferme', 'V'), ('la', 'DET'), ('porte', 'N'), 
    ('.', 'PONCT'), ('ferme', 'ADJ'), ('porte', 'V')
]

# Apprentissage du lexique à partir du corpus d'apprentissage
lexique = Apprendre_lexique(corpus_apprentissage)

# Afficher le lexique appris
print("\nLexique appris :")
for mot, etiquette in lexique.items():
    print(f"Mot: {mot}, Étiquette la plus fréquente: {etiquette}")

# Corpus de test à réétiqueter
corpus_test = [
    ('la', 'PRO'), ('belle', 'ADJ'), ('femme', 'ADJ'), 
    ('ferme', 'N'), ('la', 'PRO'), ('porte', 'V'), 
    ('.', 'PONCT')
]

# Réétiquetage du corpus de test en utilisant le lexique appris
nouveau_corpus = Retiqueter_corpus(corpus_test, lexique)

# Affichage du corpus réétiqueté
print("\nNouveau corpus réétiqueté :")
for mot, etiquette in nouveau_corpus:
    print(f"Mot: {mot}, Nouvelle étiquette: {etiquette}")

# Corpus de référence correct
corpus_reference = [
    ('la', 'DET'), ('belle', 'ADJ'), ('femme', 'N'), 
    ('ferme', 'V'), ('la', 'DET'), ('porte', 'N'), 
    ('.', 'PONCT')
]

# Comparaison du corpus réétiqueté avec le corpus de référence
nombre_erreurs = Comparer(corpus_reference, nouveau_corpus)

# Affichage du nombre d'erreurs
print(f"\nNombre d'erreurs dans le corpus réétiqueté : {nombre_erreurs}")


