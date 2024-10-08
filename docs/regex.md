# Expressions Régulières

Les expressions régulières (regex) sont un puissant outil de recherche et de manipulation de texte basé sur des motifs. Elles sont utilisées pour correspondre à des chaînes de caractères suivant des règles spécifiques.

## Variantes d'expressions régulières

Il y a plusieurs variantes de regex. Ces variantes diffèrent dans leurs syntaxes et possibilités et certains outils utilisent certaines variantes. Les variantes principales sont : 

- POSIX/GNU Basic Regular Expressions (``sed``, ``grep``)
- POSIX/GNU Extended Regular Expressions (``awk``, ``-E``)
- Perl-Compatible Regular Expressions (Perl, Python, PHP, Java)
 
POSIX a défini trois variantes, mais la plus ancienne, *simple regular expression* (SRE) est depréciée. Cependant les deux autres sont rétrocompatibles.

### POSIX Basic Regular Expressions (BRE)

Les BRE sont principalement utilisées par des outils Unix pour la rétrocompatibilité. Ainsi des outils tels que ``sed`` et ``grep`` les utilisent par défaut.

Un caractère normal ou une suite de caractères correspondent à eux même : 

- ``abcd`` : Correspond à "abcd".

Il y a plusieurs métacaractères ayant des effets particuliers: 

- ``.`` : Correspond à n'importe quel caractère sauf un saut de ligne.
- ``^`` : Début de la ligne.
- ``$`` : Fin de la ligne.
- ``*`` : Correspond à 0 ou plusieurs répétitions du caractère précédent. ``.*`` permet donc de matcher n'importe quelle série de caractères.
- ``[]`` : Définit une classe de caractères. ``[abc]`` correspond à "a", "b" ou "c". On peut aussi matcher une plage de caractères. ``[a-z]`` correspond à toutes les lettres de l'alphabet en minuscule.
- ``[^]`` : Définit une classe de caractères. ``[^abc]`` correspond à ce qui n'est pas "a", "b" ou "c".
- ``{n,m}`` : Correspond entre n et m répétitions de l'élément précédent. En BRE il faut noter ``\{n,m\}``.
- ``()``: Défini une sous-expression. Cette expression peut être rappelée plus tard avec ``\n``. En BRE il faut écrire ``\(\)``.
- ``\n`` : Permet de rappeler la n-ieme sous-expression. ``\(hello\) world \1`` matchera dans son entièreté "hello world hello".

### POSIX Extended Regular Expressions (ERE)

En ERE quasiment tout les fonctionnalités de BRE sont reprises, ``{}`` et ``()`` n'ont plus besoin d'être échapés avec des antislash ``\`` pour fonctionner. De plus ``\n`` n'est plus présent.

Il y a cependant trois nouveaux métacaractères :

- ``?`` : Correspond à 0 ou une seule fois l'élément précédent. ``ab?c`` correspondra donc avec ``ac`` ou ``abc`` par exemple.
- ``+`` : Correspond à minimum 1 fois l'élément précédent. ``ab+c`` correspondra avec ``abc`` ou encore ``abbbbc`` mais pas ``ac``.
- ``|`` : OU logique. ``abcd|efgh`` correspond à "abcd" ou "efgh".

Pour utiliser des ERE sur des outils tels que ``sed`` et ``grep`` il faut rajouter l'option ``-E`` :

```sh
echo hello world | grep -E "hello|bonjour|hola"
```

En plus de ces métacaractères, les BRE et les ERE supportent des classes de caractères :

- ``[:alnum:]`` : Caractères alphanumériques.
- ``[:alpha:]`` : Caractères alphabétiques.
- ``[:digit:]`` : Chiffres.
- ``[:lower:]`` ``[:upper:]`` : Caractères minucules et majuscules pour le second.
- ``[:space:]`` : Correspond à un espace vide, un " ", ou encore un tab, retour à la ligne...


Ces classes de caractères avec ``grep`` et ``sed`` doivent être encadrés de deux crochets : ``[[:lower:]]``. D'autres outils comme ``tr`` ne nécessitent qu'une seule paire de crochets.

### GNU vs POSIX

Il est important de noter que ``grep`` et ``sed`` sur la majorité des systèmes Linux sont en réalité ``GNU sed`` et ``GNU grep``, qui ne sont pas exactement les mêmes que ceux disponibles sur FreeBSD ou MacOS, et utilisent donc GNU BRE et GNU ERE au lieu de simplement la version POSIX.

GNU BRE et GNU ERE sont des extensions de POSIX BRE et POSIX ERE. En pratique, GNU BRE et GNU ERE fournissent les mêmes possibilités mais GNU BRE a besoin d'échapper les métacaractères seulement disponibles dans POSIX ERE.

Les opérateurs apportés par GNU BRE/ERE permettent de définir notamment les bords d'un mot :

- ``\b`` et ``\B`` : Permet de correspondre le début OU la fin d'un mot. Et pour ``\B`` de ne **pas** correspondre le début ou la fin d'un mot.
```sh
echo hello world | grep "hello\b" # => matchera
echo helloworld | grep "hello\b" # => ne matchera pas
```
- ``\>`` et ``\<``  : Permet de correspondre seulement le début d'un mot pour ``\<`` ou seulement la fin pour ``\>``.

... sur ``awk`` ``\b`` est reservé pour *backspace*, il faut donc utiliser ``\y`` à la place ...

```sh
echo hello world | awk '/hello\y/' # Renverra "hello world"
```

GNU ERE/BRE fourni aussi des raccourcis pour les classes de regex POSIX tels que ``\w`` pour les caractères alphanumériques (``\W`` pour la négation) ou encore ``\s`` pour les espaces blancs comme tabulation, espace, \r ... (``\S`` pour la négation).

### Perl-Compatible Regular Expressions (PCRE) 

Perl possède une variante d'expression régulière plus extensive que celles définies par POSIX. PCRE représente un moteur de regex basé initialement sur la syntaxe Perl et écrit en C qui permet d'implémenter cette variante de regex dans divers outils.
La syntaxe du langage Perl et du PCRE sont très proches mais pas exactement similaires. 


La force et flexibilité de cette syntaxe a poussé le PCRE a devenir un standard parmis les langages de programmation. Ainsi Python, Ruby, Java, .NET, JavaScript utilisent tous des près ou de loin la syntaxe PCRE. Certains langages tels que PHP ou R utilisent même directement le moteur PCRE.


La syntaxe PCRE récupère la syntaxe GNU ERE et y rajoute des fonctionnalités :



- ``\d`` : Correspond à un chiffre (0-9).
- ``\D`` : Correspond à un caractère non numérique.
- ``\w`` : Correspond à un caractère alphanumérique (lettres, chiffres, et underscore).
- ``\W`` : Correspond à un caractère non-alphanumérique.
- ``\s`` : Correspond à un caractère espace blanc (tab, espace, saut de ligne ...).
- ``\S`` : Correspond à un caractère non-espace blanc.

Et bien d'autres ...
[Spécification PCRE](https://www.pcre.org/original/doc/html/pcrepattern.html#SEC4)

![Variantes de REGEX](regex.png)

### Exemples Pratiques

- ``hello`` : Correspond à la chaîne "hello".

- ``\d{3}`` : Correspond à exactement trois chiffres.

- ``\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b`` : Correspond (à peu près) à une adresse email.


## Expression régulières sur Python et contournement

En Python, vous pouvez utiliser des regex pour rechercher, découper, remplacer  des motifs dans une chaîne grâce au module ``re``.

```python
import re

text = "Contactez nous à support@example.com ou contact@example.com ou thierry.amettler@proton.me"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(emails)
```

Python utilise une variante proche de la syntaxe PCRE.

Python étant un langage de programmation général il peut être judicieux de combiner des Regex avec, par exemple, des conditions ``if``, des variables ou encore des méthodes sur les strings. Cela permet potentiellement de simplifier la lecture du code qui peut vite être peu lisible avec seulement des regex.

```python
text = "Contact us at support@example.com or sales@example.com or thierry.amettler@proton.me"

def is_email(word):
    if "@" in word and "." in word:
        local, domain = word.split("@")
        if "." in domain and len(domain.split(".")[-1]) > 1:
            return True
    return False


# Extraire les mots qui sont des adresses email
words = text.split()
emails = [word for word in words if is_email(word)]
print(emails)
```
