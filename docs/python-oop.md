# Programmation Orientée Objet (POO) en Python

## Qu'est-ce que la POO ?

La Programmation Orientée Objet (POO) est un paradigme de programmation qui organise le code autour d'**objets** et de **classes**. Une **classe** définit un modèle ou un plan pour créer des objets, tandis qu'un **objet** est une instance de cette classe. La POO permet de structurer le code de manière modulaire, facilitant la réutilisation, la maintenance et l'extensibilité.

## Concepts Clés de la POO

###  Classes et Objets

- **Classe** : Un modèle définissant les propriétés (attributs) et les comportements (méthodes) que les objets créés à partir de cette classe auront.
  
```python
 class Personne:
     def __init__(self, nom, age):
         self.nom = nom
         self.age = age
 
     def saluer(self):
         print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans.")
```

- Objet : Une instance d'une classe, avec des valeurs spécifiques pour les attributs définis dans la classe.

```python
   personne1 = Personne("Alice", 30)
   personne1.saluer()  # Affiche: Bonjour, je m'appelle Alice et j'ai 30 ans.
```

#### Exercice

Créez une classe Batiment qui possède :

- Un attribut `surface_en_m2`
- Un attribut `annee_construction`
- Une méthode `construction()` qui affiche un message indiquant la construction du bâtiment
- Une méthode `description()` qui renvoie une phrase résumant les caractéristiques du bâtiment

Puis instanciez deux objets de cette classe et utilisez les méthodes / affichez les attributs.

??? Note "Solution"
    ```python
    class Batiment:
        def __init__(self, surface_en_m2, annee_construction):
            self.surface_en_m2 = surface_en_m2
            self.annee_construction = annee_construction

        def construction(self):
            print(f"Un bâtiment de {self.surface_en_m2} m² a été construit en {self.annee_construction}.")

        def description(self):
            return f"Bâtiment de {self.surface_en_m2} m², construit en {self.annee_construction}."
    ```

??? Note "Solution"
    ```python
    vieux_batiment = Batiment(surface_en_m2=90, annee_construction=1890)
    print(vieux_batiment.surface_en_m2, vieux_batiment.annee_construction)
    vieux_batiment.construction()
    print(vieux_batiment.description())

    print()

    batiment_recent = Batiment(surface_en_m2=160, annee_construction=2022)
    print(batiment_recent.surface_en_m2, batiment_recent.annee_construction)
    batiment_recent.construction()
    print(batiment_recent.description())
    ```

## Héritage

L'héritage permet de créer une nouvelle classe à partir d'une classe existante, en réutilisant et en étendant ses fonctionnalités.

```python
class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        pass

class Chien(Animal):
    def __init__(self, nom, dangereux=False):
        super().__init__(nom)
        self.dangereux = dangereux

    def parler(self):
        print(f"{self.nom} aboie.")

class Chat(Animal):
    def parler(self):
        print(f"{self.nom} miaule.")

chien = Chien("Rex")
chien.parler()  # Affiche: Rex aboie.
```

La classe enfant hérite du constructeur / ``__init__`` de la classe parent, sauf si on la redéfinit.

On peut appeler des méthodes et attributs de la classe parent dans la classe enfant avec ``super().ma_methode()`` et ``super().monattribut``.

Redéfinir `__init__` écrase celui de la classe parent, donc si on veut le récupérer on appelle `super().__init__` dans le nouveau `__init__`.

## Polymorphisme

Le polymorphisme permet d'utiliser une méthode de la même manière sur différents types d'objets, même si leur implémentation est différente.

```python
animaux = [Chien("Rex"), Chat("Mimi")]

for animal in animaux:
    animal.parler()  # Appelle la méthode `parler` spécifique à chaque classe.
```

#### Exercice

Créez une classe Maison qui hérite de Batiment et ajoute :

- Un attribut `famille` (nom de la famille habitant la maison)
- Un attribut `adresse`
- Un attribut `possede_garage` (booléen)
- Une méthode `description()`  qui étend celle de Batiment en ajoutant les infos propres à la maison

Utilisez/affichez les attributs et méthodes puis observez que les objets de classe `Maison` héritent bien d'attributs et méthodes de la classe `Batiment`.

??? Note "Solution"
    ```python
    class Maison(Batiment):
        def __init__(self, surface_en_m2, annee_construction, famille, adresse, possede_garage=False):
            super().__init__(surface_en_m2, annee_construction)
            self.famille = famille
            self.adresse = adresse
            self.possede_garage = possede_garage

        def description(self):
            garage = "avec garage" if self.possede_garage else "sans garage"
            return (f"Maison de {self.surface_en_m2} m² ({garage}), "
                    f"construite en {self.annee_construction}, "
                    f"habitée par la famille {self.famille}.")

    mamaison = Maison(surface_en_m2=50, annee_construction=1990, famille="gary", adresse="addr", possede_garage=True)
    print(mamaison.surface_en_m2)
    print(mamaison.construction())
    print(mamaison.description())
    ```

