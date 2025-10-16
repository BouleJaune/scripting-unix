# Exercices Python

## Calculer la somme des nombres dans une liste

   - **Exercice :** Écris une fonction qui prend une liste de nombres en entrée et retourne la somme de ces nombres.
   - **Exemple :**
     ```python
     def somme_liste(liste):
         # code ici
     
     print(somme_liste([1, 2, 3, 4]))  # Doit retourner 10
     ```

## Trouver le maximum dans une liste
   - **Exercice :** Écris une fonction qui prend une liste de nombres et retourne le plus grand nombre de la liste.
   - **Exemple :**
     ```python
     def max_liste(liste):
         # code ici
     
     print(max_liste([1, 7, 3, 4]))  # Doit retourner 7
     ```

## Vérifier si un nombre est pair ou impair
   - **Exercice :** Écris une fonction qui vérifie si un nombre donné est pair ou impair.
   - **Exemple :**
     ```python
     def est_pair(nombre):
         # code ici
     
     print(est_pair(4))  # Doit retourner True
     print(est_pair(7))  # Doit retourner False
     ```

## Inverser une chaîne de caractères
   - **Exercice :** Écris une fonction qui prend une chaîne de caractères et retourne cette chaîne inversée.
   - **Exemple :**
     ```python
     def inverser_chaine(chaine):
         # code ici
     
     print(inverser_chaine("Python"))  # Doit retourner "nohtyP"
     ```

## Compter les voyelles dans une chaîne de caractères
   - **Exercice :** Écris une fonction qui prend une chaîne de caractères et compte le nombre de voyelles dans cette chaîne.
   - **Exemple :**
     ```python
     def compter_voyelles(chaine):
         # code ici
     
     print(compter_voyelles("Bonjour"))  # Doit retourner 3
     ```

## Trouver la factorielle d'un nombre
   - **Exercice :** Écris une fonction qui prend un nombre entier et retourne sa factorielle.
   - **Exemple :**
     ```python
     def factorielle(n):
         # code ici
     
     print(factorielle(5))  # Doit retourner 120
     ```

## Vérifier si un nombre est un palindrome
   - **Exercice :** Écris une fonction qui vérifie si un nombre est un palindrome (il se lit de la même manière dans les deux sens).
   - **Exemple :**
     ```python
     def est_palindrome(nombre):
         # code ici
     
     print(est_palindrome(121))  # Doit retourner True
     print(est_palindrome(123))  # Doit retourner False
     ```

## Créer un motif avec des étoiles
   - **Exercice :** Écris une fonction qui prend un entier n et imprime un motif en forme de triangle d'étoiles.
   - **Exemple :**
     ```python
     def motif_etoiles(n):
         # code ici
     
     motif_etoiles(5)
     ```
   - **Sortie attendue :**
     ```markdown
     *
     **
     ***
     ****
     *****
     ```

## Remplacer les espaces par un caractère spécifique
   - **Exercice :** Écris une fonction qui remplace tous les espaces dans une chaîne de caractères par un autre caractère, par exemple, un tiret bas `_`.
   - **Exemple :**
     ```python
     def remplacer_espaces(chaine, char):
         # code ici
     
     print(remplacer_espaces("Bonjour le monde", "_"))  # Doit retourner "Bonjour_le_monde"
     ```

## Trouver le mot le plus long dans une phrase
   - **Exercice :** Écris une fonction qui prend une phrase et retourne le mot le plus long dans cette phrase.
   - **Consignes :**
     - Ignore la ponctuation.
     - Si plusieurs mots ont la même longueur, retourne le premier.
   - **Exemple :**
     ```python
     def mot_le_plus_long(phrase):
         # code ici
     
     print(mot_le_plus_long("Python est un langage de programmation génial"))  
     # Doit retourner "programmation"
     ```

## Trouver le nombre de sous-chaînes dans une chaîne
   - **Exercice :** Écris une fonction qui prend deux chaînes de caractères, `chaine` et `sous_chaine`, et retourne le nombre de fois que `sous_chaine` apparaît dans `chaine`.
   - **Consignes :**
     - La recherche doit être insensible à la casse (majuscule/minuscule).
   - **Exemple :**
     ```python
     def compter_sous_chaine(chaine, sous_chaine):
         # code ici
     
     print(compter_sous_chaine("Bonjour bonjour BONJOUR", "bonjour"))  
     # Doit retourner 3
     ```

### Réarranger les chiffres d'un nombre pour obtenir le plus grand possible
   - **Exercice :** Écris une fonction qui prend un nombre entier positif et retourne le plus grand nombre possible en réarrangeant ses chiffres. Utiliser la fonction ``sorted`` et des conversions de types.
   - **Exemple :**
     ```python
     def plus_grand_nombre_possible(nombre):
         # code ici
     
     print(plus_grand_nombre_possible(42145))  # Doit retourner 54421
     ```

## Trouver le sous-tableau avec la somme maximale

   - **Exercice :** Écris une fonction qui prend une liste de nombres (positifs et négatifs) et retourne la somme maximale possible d'un sous-tableau contigu.
   - **Consignes :**
     - Le sous-tableau peut être constitué d'un seul élément.
   - **Exemple :**
     ```python
     def somme_maximale_sous_tableau(liste):
         # code ici
     
     print(somme_maximale_sous_tableau([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  
     # Doit retourner 6 (correspondant au sous-tableau [4, -1, 2, 1])
     ```

## Vérifier si deux chaînes sont des anagrammes

   - **Exercice :** Écris une fonction qui prend deux chaînes de caractères et vérifie si elles sont des anagrammes (c'est-à-dire si elles contiennent les mêmes lettres avec la même fréquence).
   - **Exemple :**
     ```python
     def est_anagramme(chaine1, chaine2):
         # code ici
     
     print(est_anagramme("listen", "silent"))  # Doit retourner True
     print(est_anagramme("hello", "world"))    # Doit retourner False
     ```

## Créer une suite de Fibonacci jusqu'à un certain nombre
   - **Exercice :** Écris une fonction qui génère tous les nombres de la suite de Fibonacci jusqu'à ce qu'un certain nombre maximum soit atteint.
   - **Consignes :**
     - La suite de Fibonacci commence par 0 et 1, et chaque nombre suivant est la somme des deux précédents.
   - **Exemple :**
     ```python
     def suite_fibonacci(maximum):
         # code ici
     
     print(suite_fibonacci(100))  
     # Doit retourner [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
     ```

## Trouver les éléments communs entre deux listes

   - **Exercice :** Écris une fonction qui prend deux listes et retourne une liste contenant les éléments communs aux deux listes, sans duplicata.
   - **Exemple :**
     ```python
     def elements_communs(liste1, liste2):
         # code ici
     
     print(elements_communs([1, 2, 3, 4], [3, 4, 5, 6]))  # Doit retourner [3, 4]
     ```

## Déterminer si une chaîne peut être permutée en palindrome

   - **Exercice :** Écris une fonction qui prend une chaîne de caractères et détermine si elle peut être réarrangée pour former un palindrome.
   - **Exemple :**
     ```python
     def peut_devenir_palindrome(chaine):
         # code ici
     
     print(peut_devenir_palindrome("civic"))  # Doit retourner True
     print(peut_devenir_palindrome("ivicc"))  # Doit retourner True
     print(peut_devenir_palindrome("hello"))  # Doit retourner False
     ```

## Calculer le produit des autres éléments d'une liste

   - **Exercice :** Écris une fonction qui prend une liste de nombres et retourne une nouvelle liste où chaque élément est le produit de tous les autres éléments de la liste d'origine, sauf l'élément à la même position.
   - **Exemple :**
     ```python
     def produit_des_autres(liste):
         # code ici
     
     print(produit_des_autres([1, 2, 3, 4]))  # Doit retourner [24, 12, 8, 6]
     ```

