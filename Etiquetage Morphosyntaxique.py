# Importation de defaultdict pour la fonction apprendre_Etiquettes
from collections import defaultdict

################  Phase 1  ################
print('\n------------------------Phase 1-----------------------')

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


################  Phase 2  ################
print('\n------------------------Phase 2-----------------------')

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

################  Phase 3  ################
print('\n------------------------Phase 3-----------------------')

# Fonction qui applique une règle de modification d'étiquette
def Appliquer_regle(corpus, ancienne_etiquette, nouvelle_etiquette):
    """
    Applique une règle qui modifie une ancienne étiquette en une nouvelle étiquette.
    """
    nouveau_corpus = []
    for mot, etiquette in corpus:
        if etiquette == ancienne_etiquette:
            nouveau_corpus.append((mot, nouvelle_etiquette))
        else:
            nouveau_corpus.append((mot, etiquette))
    return nouveau_corpus

# Fonction qui choisit les règles en fonction des erreurs détectées et les applique
def Choisir_regles(corpus_reference, corpus_test):
    """
    Cherche les erreurs dans corpus_test par rapport au corpus_reference et applique une règle.
    Modifie les étiquettes en fonction des erreurs trouvées.
    """
    erreurs = []
    for i, ((mot_ref, etiquette_ref), (mot_test, etiquette_test)) in enumerate(zip(corpus_reference, corpus_test)):
        if etiquette_ref != etiquette_test:
            erreurs.append((i, mot_test, etiquette_test, etiquette_ref))  # Stocke l'indice, le mot, l'étiquette incorrecte et la correcte

    # Applique les corrections sur les erreurs détectées
    nouveau_corpus = corpus_test.copy()  # Copie du corpus test pour appliquer les modifications
    for i, mot, etiquette_incorrecte, etiquette_correcte in erreurs:
        # Ici, on applique simplement une règle qui remplace l'étiquette incorrecte par la correcte
        nouveau_corpus[i] = (mot, etiquette_correcte)
    
    return nouveau_corpus, erreurs

# Corpus de référence correct
corpus_reference = [
    ('la', 'DET'), ('belle', 'ADJ'), ('femme', 'N'), 
    ('ferme', 'V'), ('la', 'DET'), ('porte', 'N'), 
    ('.', 'PONCT')
]

# Corpus réétiqueté incorrect (de l'phase précédent)
corpus_test = [
    ('la', 'PRO'), ('belle', 'ADJ'), ('femme', 'ADJ'), 
    ('ferme', 'N'), ('la', 'PRO'), ('porte', 'V'), 
    ('.', 'PONCT')
]

# Application des règles de modification sur les erreurs détectées
nouveau_corpus, erreurs = Choisir_regles(corpus_reference, corpus_test)

# Affichage du corpus modifié et des erreurs détectées/corrigées
print("\nNouveau corpus après application des règles :")
for mot, etiquette in nouveau_corpus:
    print(f"Mot: {mot}, Nouvelle étiquette: {etiquette}")

print(f"\nErreurs détectées et corrigées :")
for i, mot, etiquette_incorrecte, etiquette_correcte in erreurs:
    print(f"Mot: {mot}, Étiquette incorrecte: {etiquette_incorrecte}, Étiquette correcte: {etiquette_correcte}")


################  Phase 4  ################
print('\n------------------------Phase 4-----------------------')

### Génération des règles jusqu'à un seuil d'erreurs ###
def Generer_regles(corpus_reference, corpus_test, seuil):
    erreurs_actuelles = Comparer(corpus_reference, corpus_test)  # Initialisation des erreurs
    regles = []  # Liste des règles appliquées
    
    while erreurs_actuelles > seuil:
        # Appliquer les règles et obtenir le nouveau corpus et les erreurs
        corpus_test, erreurs = Choisir_regles(corpus_reference, corpus_test)
        
        # Enregistrer les règles appliquées (sauvegarde des corrections)
        for i, mot, etiquette_incorrecte, etiquette_correcte in erreurs:
            regles.append(f"Remplacer {etiquette_incorrecte} par {etiquette_correcte} pour le mot '{mot}'")
        
        # Recalculer le nombre d'erreurs après correction
        erreurs_actuelles = Comparer(corpus_reference, corpus_test)
    
    return regles, corpus_test

# Test avec le corpus_reference et corpus_test
# Corpus de référence correct
corpus_reference = [
    ('la', 'DET'), ('belle', 'ADJ'), ('femme', 'N'), 
    ('ferme', 'V'), ('la', 'DET'), ('porte', 'N'), 
    ('.', 'PONCT')
]
# Corpus de test incorrect à corriger
corpus_test = [
    ('la', 'PRO'), ('belle', 'ADJ'), ('femme', 'ADJ'), 
    ('ferme', 'N'), ('la', 'PRO'), ('porte', 'V'), 
    ('.', 'PONCT')
]
# Définir un seuil d'erreurs acceptable
seuil = 1  # Par exemple, on veut moins d'une erreur

# Générer les règles et corriger le corpus
regles_appliquees, corpus_corrige = Generer_regles(corpus_reference, corpus_test, seuil)

# Affichage des règles appliquées
print("\nRegles appliquees :")
for regle in regles_appliquees:
    print(regle)

# Affichage du corpus corrigé
print("\nCorpus corrige :")
for mot, etiquette in corpus_corrige:
    print(f"Mot: {mot}, Etiquette: {etiquette}")

# Nombre final d'erreurs
nombre_erreurs = Comparer(corpus_reference, corpus_corrige)
print(f"\nNombre d'erreurs apres correction : {nombre_erreurs}")


################  Phase 5  ################
print('\n------------------------Phase 5-----------------------')

# Fonction pour étiqueter un corpus avec un lexique et appliquer des règles
def Etiqueter_corpus(corpus_test, lexique, liste_regles):
    # Initialisation du corpus avec le lexique
    nouveau_corpus = Retiqueter_corpus(corpus_test, lexique)

    # Application des règles de réétiquetage
    for regle in liste_regles:
        ancienne_etiquette, nouvelle_etiquette = regle  # Chaque règle contient l'ancienne et la nouvelle étiquette
        nouveau_corpus = Appliquer_regle(nouveau_corpus, ancienne_etiquette, nouvelle_etiquette)

    return nouveau_corpus

# Exemple d'utilisation
# Lexique appris
lexique = {
    'la': 'DET', 'belle': 'ADJ', 'femme': 'N', 'ferme': 'V', 'porte': 'N', '.': 'PONCT'
}

# Liste de règles à appliquer (ancienne étiquette -> nouvelle étiquette)
liste_regles = [('ADJ', 'N'), ('PRO', 'DET')]  # Exemple de règles

# Corpus à tester
corpus_test = [
    ('la', 'PRO'), ('belle', 'ADJ'), ('femme', 'ADJ'), 
    ('ferme', 'N'), ('la', 'PRO'), ('porte', 'V'), 
    ('.', 'PONCT')
]

# Appel de la fonction Etiqueter_corpus
nouveau_corpus = Etiqueter_corpus(corpus_test, lexique, liste_regles)

# Affichage du résultat final
print("\nCorpus final après application des règles :")
for mot, etiquette in nouveau_corpus:
    print(f"Mot: {mot}, Étiquette: {etiquette}")
