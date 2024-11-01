# Analyse et Réétiquetage de Corpus de Texte

Ce code implémente une série de fonctions pour l'analyse, l'apprentissage et la correction d'étiquettes sur un corpus de texte. Il utilise un processus en plusieurs phases pour créer un lexique, réétiqueter un corpus et corriger les erreurs d'étiquetage en appliquant des règles de réétiquetage.

## Fonctionnalités

### Phase 1 : Apprentissage des Étiquettes
- **Fonction `apprendre_Etiquettes`** : apprend l'étiquette la plus fréquente pour chaque mot dans un corpus donné.
- **Fonction `Apprendre_lexique`** : génère un lexique basé sur les étiquettes apprises.

### Phase 2 : Réétiquetage et Comparaison
- **Fonction `Retiqueter_corpus`** : réétiquette un corpus de test à partir d'un lexique.
- **Fonction `Comparer`** : compare deux corpus et compte les erreurs d'étiquetage.

### Phase 3 : Application de Règles
- **Fonction `Appliquer_regle`** : applique une règle de correction sur les étiquettes d'un corpus.
- **Fonction `Choisir_regles`** : détecte et corrige les erreurs d'étiquetage en appliquant les règles nécessaires.

### Phase 4 : Génération Automatique de Règles
- **Fonction `Generer_regles`** : génère des règles pour corriger un corpus jusqu'à atteindre un seuil d'erreurs acceptable.

### Phase 5 : Étiquetage Final avec Règles
- **Fonction `Etiqueter_corpus`** : applique les étiquettes et règles pour obtenir un corpus corrigé final.

