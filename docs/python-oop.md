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

### Encapsulation

L'encapsulation est la technique consistant à restreindre l'accès direct à certains attributs ou méthodes d'un objet, en les protégeant avec des méthodes d'accès (getters) et de modification (setters).

```python
class CompteBancaire:
    def __init__(self, solde):
        self.__solde = solde  # Attribut privé

    def deposer(self, montant):
        self.__solde += montant

    def retirer(self, montant):
        if montant <= self.__solde:
            self.__solde -= montant
        else:
            print("Fonds insuffisants")

    def afficher_solde(self):
        print(f"Solde: {self.__solde}")
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
    def parler(self):
        print(f"{self.nom} aboie.")

class Chat(Animal):
    def parler(self):
        print(f"{self.nom} miaule.")

chien = Chien("Rex")
chien.parler()  # Affiche: Rex aboie.
```

## Polymorphisme

Le polymorphisme permet d'utiliser une méthode de la même manière sur différents types d'objets, même si leur implémentation est différente.

```python
animaux = [Chien("Rex"), Chat("Mimi")]

for animal in animaux:
    animal.parler()  # Appelle la méthode `parler` spécifique à chaque classe.
```

## Abstraction

L'abstraction consiste à définir des classes de base (souvent des classes abstraites) qui ne sont pas destinées à être instanciées, mais à être héritées par d'autres classes.

```python
from abc import ABC, abstractmethod

class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass

class Carre(Forme):
    def __init__(self, cote):
        self.cote = cote

    def aire(self):
        return self.cote ** 2
```
